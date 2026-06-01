from src.voice.text_to_speech import speak

for i in range(5):
    print(f"Speaking {i}")
    speak(f"This is test number {i}")