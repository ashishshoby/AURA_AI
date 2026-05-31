from src.brain.intent_classifier import classify_intent

while True:

    command = input("> ")

    print(
        classify_intent(command)
    )