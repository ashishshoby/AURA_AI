import ollama
import time

MODEL = "qwen3:8b"
TIMEOUT_SECONDS = 60


def ask_heavy(prompt):

    start = time.perf_counter()

    print("[AURA] Thinking...")

    try:
        client = ollama.Client(timeout=TIMEOUT_SECONDS)

        response = client.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "num_predict": 512,
                "temperature": 0.2,
                "num_ctx": 4096
            }
        )

        return response["message"]["content"]

    except Exception as e:
        print("Heavy Brain Error:", e)
        return "I couldn't reach my heavy brain right now."

    finally:
        print(
            f"LLM Response Time: {round(time.perf_counter() - start, 2)} sec"
        )
