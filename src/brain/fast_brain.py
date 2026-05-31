import ollama
import time

MODEL = "llama3.2:3b"
TIMEOUT_SECONDS = 30


def ask_fast(prompt):
    start = time.perf_counter()

    print("[AURA] Thinking...")

    try:
        client = ollama.Client(timeout=TIMEOUT_SECONDS)

        response = client.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                        "content": (
                            "You are Aura AI.\n\n"
                            "Speak like a helpful voice assistant.\n\n"
                            "Keep answers short, conversational, and voice friendly.\n\n"
                            "Use 2 to 3 sentences at most.\n\n"
                            "Do not use markdown.\n"
                            "Do not use bullet points.\n"
                            "Do not use code blocks."
                        ),
                },
                {"role": "user", "content": prompt},
            ],
            options={
                "num_predict": 40,
                "temperature": 0.2,
                "num_ctx": 1024
            }
        )

        return response["message"]["content"]

    except Exception as e:
        print("Fast Brain Error:", e)
        return "I couldn't reach my fast brain right now."

    finally:
        print(
            f"LLM Response Time: {round(time.perf_counter() - start, 2)} sec"
        )
