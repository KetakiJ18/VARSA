import os
import datetime
import webbrowser
from core.speech import speak, listen
from commands.file_opener import open_file_command
from commands.spotify import focus_spotify_and_play_pause
from commands.weather import get_weather
import pyautogui

def handle_command(command):
    if "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")
        return {"status": "opened", "message": "Opened Notepad"}

    elif "open browser" in command:
        speak("Opening your browser.")
        webbrowser.open("https://www.google.com")
        return {"status": "opened", "message": "Opened Browser"}

    elif "what time is it" in command or "tell me the time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is {now}.")
        return {"status": "info", "message": f"The time is {now}"}
    
    elif "open clock" in command:
        speak("Opening Clock.")
        os.system("start ms-clock:")
        return {"status": "opened", "message": "Opened Clock"}

    elif "open spotify" in command:
        speak("Opening Spotify.")
        os.system("start spotify:")
        return {"status": "opened", "message": "Opened Spotify"}

    elif command.startswith("open file"):
        return open_file_command(command)

    elif "exit" in command or "quit" in command or "thank you" in command:
        speak("Adios Amigos! Until next time.")
        return {"status": "exit", "message": "Goodbye!"}

    elif "pause music" in command or "stop music" in command:
        speak("Pausing music.")
        focus_spotify_and_play_pause()
        return {"status": "success", "message": "Paused music"} #when spotify is focused

    elif "resume music" in command or "play music" in command:
        speak("Resuming music.")
        focus_spotify_and_play_pause()
        return {"status": "success", "message": "Resumed music"}

    elif "next song" in command or "next track" in command:
        speak("Skipping to next song.")
        pyautogui.hotkey('ctrl', 'right')
        return {"status": "success", "message": "Skipped to next song"}

    elif "previous song" in command or "go back" in command:
        speak("Playing previous song.")
        pyautogui.hotkey('ctrl', 'left')
        return {"status": "success", "message": "Went to previous song"}
    
    elif "weather" in command or "temperature" in command:
        speak("Checking the weather...")
        weather_info=get_weather()  # default is Mumbai
        return {"status": "success", "message": weather_info}
        
    else:
        speak(f"You said: {command}")
        return {"status": "error", "message": "Unrecognized command"}

if __name__ == "__main__":
    speak("Hiii there! I'm VARSA! Ready to serve")
    while True:
        command = listen()
        if command:
            result = handle_command(command)
            if result.get("status") == "exit":
                break
