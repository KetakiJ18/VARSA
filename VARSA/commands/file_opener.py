import os
from core.speech import speak, listen
from core.config import SEARCH_FOLDERS, word_to_number

def find_all_matches(filename):
    matches = []
    filename = filename.lower()
    for folder in SEARCH_FOLDERS:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if filename in file.lower():
                    matches.append(os.path.join(root, file))
                    if len(matches) >= 5:
                        return matches
    return matches

def open_file_command(command):
    filename = command.replace("open file", "").strip()
    if filename:
        speak(f"Searching for files named {filename}.")
        matches = find_all_matches(filename)

        if not matches:
            speak(f"Sorry, I couldn't find any files with that name.")
        elif len(matches) == 1:
            os.startfile(matches[0])
            speak(f"Opening {os.path.basename(matches[0])}")
        else:
            speak(f"I found {len(matches)} files. Please say the number you want to open.")
            for i, path in enumerate(matches, 1):
                print(f"{i}. {os.path.basename(path)}")

            while True:
                try:
                    choice = listen().lower()
                    if "cancel" in choice:
                        speak("Okay, cancelled the operation.")
                        break

                    index = None
                    for word in choice.split():
                        if word.isdigit():
                            index = int(word)
                            break
                        elif word in word_to_number:
                            index = word_to_number[word]
                            break

                    if index and 1 <= index <= len(matches):
                        os.startfile(matches[index - 1])
                        speak(f"Opening {os.path.basename(matches[index - 1])}")
                        break
                    else:
                        speak("Sorry, I didn't catch a valid number. Please try again.")
                except:
                    speak("Something went wrong. Please try again.")
