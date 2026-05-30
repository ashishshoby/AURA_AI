import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.2
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        except sr.WaitTimeoutError:

            return None

    try:

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:

        print("Could not understand audio")

        return None

    except sr.RequestError:

        print("Internet connection error")

        return None