# AURA AI

AURA AI is a Windows-focused desktop voice assistant built in Python. It listens for spoken commands, responds with text-to-speech, opens and closes applications, searches local documents, controls system utilities, manages music playback, and routes general questions to local Ollama models.

The project is currently a functional prototype with multiple implemented desktop automation features and an expanding roadmap toward a richer personal operating-system assistant.

## Current Status

Project stage: active prototype.

Implemented areas include:

- Voice input and voice output
- Desktop application launching and closing
- Running application discovery
- Local file and document search
- Document text extraction for indexed search
- Conversational AI using Ollama
- Fast and heavy brain routing
- System status checks
- Volume control
- Screenshot capture
- Process monitoring and termination
- Spotify and media playback control
- Windows power commands
- Basic validation scripts and manual test files

## Core Features

### Voice Assistant

AURA continuously listens through the microphone and handles recognized speech commands.

Implemented in:

- `src/voice/speech_to_text.py`
- `src/voice/text_to_speech.py`
- `main.py`

Capabilities:

- Captures microphone input using `SpeechRecognition`
- Uses Google speech recognition for speech-to-text
- Responds using `pyttsx3`
- Prints recognized commands and response timing in the terminal
- Runs in a continuous listening loop

Example commands:

- `hello`
- `who are you`
- `what time is it`
- `what is the date`
- `exit`

### Application Control

AURA can open and close desktop applications using Start Menu shortcuts, known aliases, Windows built-ins, and Microsoft Store app IDs.

Implemented in:

- `src/apps/app_manager.py`
- `src/apps/app_scanner.py`
- `src/apps/app_database.py`
- `src/apps/store_apps.py`
- `src/apps/running_apps.py`

Capabilities:

- Opens apps from Start Menu `.lnk` shortcuts
- Opens built-in Windows apps such as Notepad and Calculator
- Supports aliases such as `chrome`, `vscode`, `edge`, `vlc`, `github`, and `telegram`
- Opens Microsoft Store apps through PowerShell `Get-StartApps`
- Closes apps by mapped process names or fuzzy process matching
- Lists currently running non-system apps
- Builds a process cache on startup

Example commands:

- `open chrome`
- `launch vscode`
- `start calculator`
- `close chrome`
- `close notepad`
- `what apps are running`

### File Search and Document Understanding

AURA can build a searchable local file index and search files by name or extracted document content.

Implemented in:

- `build_index.py`
- `src/file_search/indexer.py`
- `src/file_search/search_engine.py`
- `src/file_search/document_parser.py`
- `src/file_search/search_memory.py`
- `src/file_search/file_opener.py`

Capabilities:

- Indexes files from Documents, Desktop, and Downloads
- Extracts text from supported document types
- Searches file names with RapidFuzz matching
- Searches indexed file content
- Supports topic-style document queries
- Stores recent search results so they can be opened by number
- Falls back to live drive search if the index is missing

Supported file types:

- `.pdf`
- `.docx`
- `.pptx`
- `.txt`
- `.html`
- `.doc` is listed in the indexer/search filters, but full parsing support depends on the parser implementation

Example commands:

- `find resume`
- `search for network notes`
- `find pdfs about cybersecurity`
- `search documents related to data mining`
- `open result 1`

To rebuild the file index:

```bash
python build_index.py
```

The generated index is stored at:

```text
data/file_index.json
```

### AI Brain and Chat Mode

AURA uses local Ollama models for general questions and conversational responses.

Implemented in:

- `src/brain/brain.py`
- `src/brain/router.py`
- `src/brain/fast_brain.py`
- `src/brain/heavy_brain.py`
- `src/brain/chat.py`
- `src/brain/intent_classifier.py`

Capabilities:

- Routes normal questions to a fast local model
- Routes document analysis, project analysis, summarization, and detailed reasoning prompts to a heavier model
- Keeps the last few conversation turns in chat memory
- Supports explicit chat mode
- Clears chat history when chat mode is stopped

Current model configuration:

- Fast brain: `llama3.2:3b`
- Heavy brain: `qwen3:8b`

Example commands:

- `what is data mining`
- `explain machine learning`
- `summarize document`
- `analyze this project`
- `start chat mode`
- `stop chat mode`

### System Information

AURA can report basic system status.

Implemented in:

- `src/system/system_info.py`

Capabilities:

- Battery percentage and charging status
- CPU usage
- RAM usage
- C drive disk space
- Internet connectivity check

Example commands:

- `battery`
- `cpu usage`
- `ram usage`
- `memory status`
- `disk space`
- `wifi status`
- `internet status`

### Volume Control

AURA can control the Windows speaker volume.

Implemented in:

- `src/system/volume_control.py`

Capabilities:

- Increase volume
- Decrease volume
- Mute audio
- Unmute audio
- Set volume to a specific percentage

Example commands:

- `volume up`
- `volume down`
- `mute`
- `unmute`
- `set volume to 50`

### Screenshot Capture

AURA can capture and save screenshots.

Implemented in:

- `src/system/screenshot.py`

Capabilities:

- Captures the current screen using `pyautogui`
- Saves screenshots to the user's Pictures folder

Save location:

```text
~/Pictures/Aura Screenshots
```

Example commands:

- `take screenshot`
- `capture screen`
- `screenshot`

### Process Manager

AURA can inspect and terminate running processes.

Implemented in:

- `src/system/process_manager.py`

Capabilities:

- Shows top CPU-consuming processes
- Shows top RAM-consuming processes
- Kills matching processes by name

Example commands:

- `top processes`
- `cpu hungry apps`
- `ram hungry apps`
- `memory hungry apps`
- `kill chrome`

### Music and Spotify Control

AURA can open Spotify, search Spotify, and control media playback.

Implemented in:

- `src/music/music_controller.py`

Capabilities:

- Opens Spotify
- Searches Spotify using the Spotify URI scheme
- Sends media key commands for play/pause, next, and previous track

Example commands:

- `open spotify`
- `search spotify for faded`
- `play music`
- `pause music`
- `next song`
- `previous song`

### Power Commands

AURA can run Windows power-management commands.

Implemented in:

- `src/system/power_manager.py`

Capabilities:

- Lock computer
- Shut down computer
- Restart computer
- Put computer to sleep

Example commands:

- `lock pc`
- `shutdown pc`
- `restart pc`
- `sleep pc`

Warning: shutdown and restart commands execute immediately.

## Project Structure

```text
AURA AI/
|-- main.py
|-- build_index.py
|-- requirements.txt
|-- README.md
|-- data/
|   `-- file_index.json
|-- docs/
|   `-- day 2.md
|-- src/
|   |-- apps/
|   |-- brain/
|   |-- core/
|   |-- file_search/
|   |-- music/
|   |-- system/
|   `-- voice/
`-- tests/
```

## Installation

### 1. Clone or open the project

```bash
cd "d:\1\AURA AI"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Command Prompt:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

Some implemented modules also import these packages, so install them if they are not already present:

```bash
pip install ollama keyboard pyautogui pycaw
```

PyAudio can require platform-specific setup on Windows. If normal installation fails, install a compatible wheel for your Python version.

### 5. Install and prepare Ollama models

Install Ollama, start the Ollama service, then pull the configured models:

```bash
ollama pull llama3.2:3b
ollama pull qwen3:8b
```

### 6. Build the document index

```bash
python build_index.py
```

### 7. Run AURA

```bash
python main.py
```

## Testing and Validation

The repository includes small manual test scripts and a validation checklist.

Run the validation checklist:

```bash
python tests/validation_checklist.py
```

Run selected manual tests:

```bash
python test_voice.py
python test_search.py
python test_brain.py
python test_apps.py
```

Many tests interact with the local machine, microphone, installed apps, audio output, Ollama, or Windows APIs. Results can vary depending on the system environment.

## Current Limitations

- The assistant is designed mainly for Windows.
- Speech recognition depends on internet access because it uses Google recognition through `SpeechRecognition`.
- Ollama must be installed and running for AI chat responses.
- Some commands use immediate system actions, including shutdown and restart.
- File indexing currently scans Documents, Desktop, and Downloads only.
- Search is keyword/fuzzy based, not semantic vector search yet.
- Chat memory is in-memory only and resets when the program exits.
- Some command matching is rule-based and may require exact phrasing.
- `requirements.txt` may need the extra packages listed above for all implemented modules.

## Future Features

Planned and recommended future improvements:

- Wake word support such as `Hey Aura`
- Offline speech recognition
- More natural command parsing with intent confidence
- Safer confirmation prompts for shutdown, restart, sleep, and process killing
- Semantic file search using embeddings and vector storage
- Document summarization from selected search results
- Persistent long-term memory
- User preferences and personalization
- GUI dashboard for status, commands, and search results
- Tray app mode
- Calendar and reminder integration
- Email and message drafting
- Browser automation
- Screen understanding and visual question answering
- OCR for screenshots and images
- Smarter app detection and launch ranking
- Background file index refresh
- Better logging and error reporting
- Unit tests with mocks for system APIs
- Configuration file for models, folders, aliases, and command behavior
- Plugin system for adding new skills
- Multi-language voice input and output
- Secure permissions layer for sensitive actions

## Development Notes

Main command routing happens in:

```text
src/core/intent_handler.py
```

The application starts from:

```text
main.py
```

The file indexer starts from:

```text
build_index.py
```

When adding a new feature, the usual flow is:

1. Add the implementation under the relevant `src/` module.
2. Add command handling in `src/core/intent_handler.py`.
3. Add or update a test script.
4. Update this README with the new command examples.

## License

No license file is currently included. Add a license before distributing or publishing the project.
