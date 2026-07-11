import asyncio

from src.script_narrator.edge_engine import generate_speech


async def main() -> None:
    script = (
        "Welcome back to Coding With Atlas. "
        "Today, I am building my own script narration application."
    )

    output_path = await generate_speech(
        text=script,
        output_file="output/narration.mp3",
    )

    print(f"Narration saved to: {output_path}")


if __name__ == "__main__":
    asyncio.run(main())