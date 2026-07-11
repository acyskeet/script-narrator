# Script Narrator

A simple Python application that turns written scripts into natural-sounding narration.

The project currently uses Microsoft Edge TTS and is being built with video narration, tutorials, and content creation in mind.

## Project Status

This project is in early development.

The current version can:

* Convert text into speech
* Use the `en-US-AndrewNeural` voice
* Save generated narration as an MP3 file
* Run locally through Python

Planned features include:

* A desktop graphical interface
* Script editing
* Voice selection
* Speaking-rate, pitch, and volume controls
* Audio previews
* Custom output filenames
* WAV and MP3 export
* Long-script handling
* An optional offline Piper voice engine

## Requirements

* Python 3.10 or newer
* An internet connection for Edge TTS
* FFmpeg for future audio-processing features

The project has currently been tested on Fedora Linux with Python 3.14.

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd script-narrator
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install edge-tts
```

## Usage

Run the program:

```bash
python main.py
```

The generated narration will be saved as:

```text
narration.mp3
```

## Current Default Voice

The current default voice is:

```text
en-US-AndrewNeural
```

The default voice may become configurable in a future version.

## Why This Project Exists

This project is being built as an accessible narration tool for people who want to create videos without recording their own voice.

It is also a learning project focused on Python, desktop application development, audio processing, and open-source development.

## Contributing

The project is still in its earliest stage, but suggestions and issue reports are welcome.

## License

A license will be added before the first stable release.
