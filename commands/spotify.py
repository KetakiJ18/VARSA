import pyautogui
import pygetwindow as gw
import time

def focus_spotify_and_play_pause():
    try:
        spotify = None
        for window in gw.getWindowsWithTitle('Spotify'):
            if "Spotify" in window.title:
                spotify = window
                break

        if spotify:
            spotify.activate()
            time.sleep(0.5)  # Let it focus
            pyautogui.press('space')  # Toggle playback
        else:
            print("Spotify window not found.")
    except Exception as e:
        print(f"Error: {e}")
