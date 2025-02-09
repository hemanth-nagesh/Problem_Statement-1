import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

# Google API
genai.configure(api_key="YOUR-API-KEY-HERE")

# model instruction
instruction = "You are an helpful spoken english AI voice assistant. speack like one."

#initialize model
model = genai.GenerativeModel(
    "models/gemini-2.0-flash", system_instruction=instruction
)
# Initialize the text-to-speech engine
engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
            audio = recognizer.record(source)  # Load audio
        text = recognizer.recognize_google(audio)
        print(f"Transcription successful: {text}")
        return text
    
    except Exception as e:
        print(f"Unexpected error during transcription: {e}")
        return None

def generate_response(prompt):
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

def speak_text(text):
    voice_id=1
    # voice properties
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voice_id].id)    
    engine.setProperty("rate", 190)  # speed
    engine.setProperty("volume", 0.8)  # volume

    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()
    print("'Genius' is Active now...")
    speak_text("Genius is Active now...")
    while True:
        try:
            print("say something....")
            filename = "input.wav"
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)

            # Save recorded audio
            with open(filename, "wb") as f:
                f.write(audio.get_wav_data())

            # Transcribe Audio to Text
            text = transcribe_audio_to_text(filename)
            if text:
                print(f"You said: {text}")

                # LLM Response
                response = generate_response(text)
                print(f"LLM says: {response}")

                # Read Response Using TTS
                speak_text(response)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio. Try again.")
            speak_text("Sorry, I couldn't understand the audio. Try again.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition service error: {e}")
            speak_text("Google Speech Recognition service error")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak_text("An error occurred")

if __name__ == "__main__":
    main()
