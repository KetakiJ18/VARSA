import os
from pathlib import Path

USER_HOME = Path.home()

SEARCH_FOLDERS = [
    USER_HOME / "Desktop",
    USER_HOME / "Documents",
    USER_HOME / "Downloads",
    USER_HOME / "Music",
    USER_HOME / "Pictures",
    USER_HOME / "OneDrive",  #only if onedrive is available on the machine..
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
} #to select the particular files 
