# test_edge_tts.py

import asyncio
import edge_tts
import os

async def main():

    text = "Hello Ashish. Aura is speaking."

    communicate = edge_tts.Communicate(
        text,
        voice="en-US-AriaNeural"
    )

    await communicate.save("aura_test.mp3")

    os.startfile("aura_test.mp3")

asyncio.run(main())