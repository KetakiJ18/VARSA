import speech_recognition as sr
import pyttsx3
import threading

engine=pyttsx3.init()
engine_lock = threading.Lock()

def speak(text):
    with engine_lock:
        engine.say(text)
        engine.runAndWait()  #listens while being spoken to

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("VARSA listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Speech service unavailable.")
        speak("Speech service is unavailable.")
        return ""