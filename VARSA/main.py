import os, datetime,webbrowser
from core.speech import speak,listen 
from commands.file_opener import open_file_command

def handle_command(command):
    if "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")
        return True

    elif "open browser" in command:
        speak("Opening your browser.")
        webbrowser.open("https://www.google.com")
        return True

    elif "what time is it" in command or "tell me the time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is {now}.")
        return True

    elif "play music" in command:
        speak("Playing music.")
        music_path = r"C:\Users\ketak\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\Spotify.exe"
        os.startfile(music_path)
        return True

    elif command.startswith("open file"):
        open_file_command(command)
        return True

    elif "exit" in command or "quit" in command or "stop" in command or "thank you" in command:
        speak("Adios Amigos! Until next time")
        return False

    else:
        speak("Sorry, I didn't get that")
        return True


if __name__ == "__main__":
    speak("Wassup amigo! I'm VARSA! Ready to serve")
    while True:
        command = listen()
        if command:
            if not handle_command(command):
                break
