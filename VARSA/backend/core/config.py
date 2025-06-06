import os

USERNAME = os.getlogin()
SEARCH_FOLDERS = [
    fr"C:\Users\{USERNAME}\Desktop",
    fr"C:\Users\{USERNAME}\Documents",
    fr"C:\Users\{USERNAME}\Downloads",
    fr"C:\Users\{USERNAME}\Music",
    fr"C:\Users\{USERNAME}\Pictures",
    fr"C:\Users\{USERNAME}\OneDrive"
]

word_to_number = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}
