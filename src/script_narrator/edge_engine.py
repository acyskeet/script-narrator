from pathlib import Path

import edge_tts


DEFAULT_VOICE = "en-US-AndrewNeural"


async def generate_speech(
    text: str,
    output_file: str | Path,
    voice: str = DEFAULT_VOICE,
) -> Path:
    """Generate an MP3 narration file using Microsoft Edge TTS."""

    cleaned_text = text.strip()

    if not cleaned_text:
        raise ValueError("The script cannot be empty.")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    communication = edge_tts.Communicate(
        text=cleaned_text,
        voice=voice,
    )

    await communication.save(str(output_path))

    return output_path