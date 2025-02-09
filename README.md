## Problem_Statement-1
# AI Voice Assistant

An intelligent voice assistant that combines speech recognition, natural language processing, and text-to-speech capabilities to create an interactive conversational experience. The assistant can understand spoken commands, process them using Google's Gemini AI model, and respond with synthesized speech.

## Features

- Real-time speech recognition with noise reduction
- Natural language processing using Google's Gemini 2.0 Flash model
- High-quality text-to-speech conversion
- Continuous conversation capability
- Robust error handling for reliable operation

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.8 or higher
- Google Cloud API credentials
- Internet connection for speech recognition and AI model access

## Required Dependencies

```bash
pip install google-generativeai
pip install pyttsx3
pip install SpeechRecognition
```

## Configuration

1. Obtain a Google Cloud API key from the Google Cloud Console
2. Configure the API key in the code:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/hemanth-nagesh/Problem_Statement-1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the assistant:
   ```bash
   python main.py
   ```

4. Start speaking when prompted with "say something..."

## System Architecture

The assistant operates through three main layers:

1. **Speech-to-Text (STT) Layer**
   - Utilizes Google's speech recognition service
   - Implements noise reduction for better accuracy
   - Saves audio input as temporary WAV files

2. **Language Model (LLM) Layer**
   - Powered by Google's Gemini 2.0 Flash model
   - Processes natural language input
   - Generates contextually appropriate responses

3. **Text-to-Speech (TTS) Layer**
   - Uses pyttsx3 engine for speech synthesis
   - Configurable voice properties (speed, volume, voice type)
   - Natural-sounding voice output

## License

This project is for personal use only.

## Acknowledgments

- Google Cloud Platform for AI and Speech Recognition services
- pyttsx3 developers for the TTS engine
- SpeechRecognition library contributors
