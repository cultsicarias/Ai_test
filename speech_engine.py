import asyncio
import threading
import edge_tts
import speech_recognition as sr
import os
from playsound import playsound
from ui_utils import update_log

async def async_speak(text, output_file="voice.mp3"):
    try:
        communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
        await communicate.save(output_file)
        playsound(output_file)
        os.remove(output_file)  # Clean up temp file
    except Exception as e:
        print("Voice error:", e)

def speak(text):
    threading.Thread(target=lambda: asyncio.run(async_speak(text)), daemon=True).start()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        update_log("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
            command = recognizer.recognize_google(audio)
            update_log(f"🗣️ You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            update_log("⏱️ No speech detected.")
            return ""
        except sr.UnknownValueError:
            update_log("❓ Didn't catch that.")
            return ""
        except sr.RequestError:
            update_log("⚠️ Google service error.")
            return ""

