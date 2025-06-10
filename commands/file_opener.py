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
                    if len(matches) >= 100:
                        return matches
    return matches

def open_file_command(command):
    filename = command.replace("open file", "").strip()
    if filename:
        speak(f"Searching for files named {filename}.")
        matches = find_all_matches(filename)

        if not matches:
            speak(f"Sorry, I couldn't find any files with that name.")
            return {"status": "no_files", "message": "No files found."}
        else:
            speak(f"I found {len(matches)} files. Please select one")
            # OPENS the file paths only.. not the actual files
            return {"status": "file_list", "files": matches, "message": f"Found {len(matches)} files. Please select one."}
    else:
        speak("Please specify the file name.")
        return {"status": "error", "message": "No filename specified."}