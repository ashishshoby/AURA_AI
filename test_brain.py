print("Starting...")

from src.brain.brain import ask_brain

print("Imported")

response = ask_brain(
    "What is Data Mining?"
)

print("Response received")

print(response)