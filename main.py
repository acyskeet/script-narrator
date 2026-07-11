import asyncio

import edge_tts


VOICE = "en-US-AndrewNeural"
OUTPUT_FILE = "narration.mp3"


async def generate_speech(text: str) -> None:
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
    )

    await communicate.save(OUTPUT_FILE)
    print(f"Saved narration to {OUTPUT_FILE}")


async def main() -> None:
    script = (
        "Welcome back to Coding With Atlas. "
        "Today, I am building my own script narration application."
    )

    await generate_speech(script)


if __name__ == "__main__":
    asyncio.run(main())