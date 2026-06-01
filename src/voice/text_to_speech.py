import pyttsx3

def speak(text):

    print(f"AURA: {text}")

    try:

        engine = pyttsx3.init()

        voices = engine.getProperty("voices")

        if len(voices) > 1:
            engine.setProperty(
                "voice",
                voices[1].id
            )

        engine.setProperty(
            "rate",
            180
        )

        engine.setProperty(
            "volume",
            1.0
        )

        engine.say(str(text))

        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print(
            "TTS Error:",
            e
        )