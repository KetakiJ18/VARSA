import requests
from core.speech import speak

def get_weather(city="Mumbai"): #default city is mumbai
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        
        if response.status_code == 200:
            report = response.text  
            speak(f"Weather update: {report}")
            return report
        else:
            speak("Sorry, I couldn't fetch the weather right now.")
    except Exception as e:
        speak("Something went wrong while checking the weather.")
        print(f"Error: {e}")
    