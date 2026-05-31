from src.brain.router import ask_brain

while True:

    q = input("> ")

    print(
        ask_brain(q)
    )