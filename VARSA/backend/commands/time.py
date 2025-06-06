import time
from core.speech import speak
def set_reminder(reminder, seconds):
    speak(f"Setting a reminder for {reminder} in {seconds} seconds.")
    time.sleep(seconds)
    speak(f"Reminder: {reminder}")