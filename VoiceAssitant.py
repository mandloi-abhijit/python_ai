import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import subprocess
import time


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            
            return data
        except sr.UnknownValueError:
            print("Did not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say(x)
    engine.runAndWait()
def open_app(app_path):
    try:
        subprocess.Popen(app_path)
        speechtx(f"{app_path} is opening now")
    except FileNotFoundError:
        speechtx(f"Could not find {app_path}")
        

if __name__ == '__main__':
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' 
    chrome = webbrowser.get(chrome_path)

    if "hey friday" in sptext().lower():
        while True:
            data1 = sptext()
            if data1 is None:  # If no command was recognized
                continue
            
            if "my name" in data1:
                name = "your name is Abhijit"
                speechtx(name)
            elif "old are you" in data1:
                age = "I am two years old"
                speechtx(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1:
                chrome.open("youtube.com") 
                speechtx("opening youtube")
            elif "netflix" in data1:
                chrome.open("netflix.com")
                speechtx("opening netflix")
            elif "weather" in data1:
                speechtx("here's the weather")
                chrome.open("https://www.accuweather.com/en/in/indore/204411/weather-forecast/204411")
            elif "joke" in data1:
                joke_1 = pyjokes.get_jokes(language="en",category='all')
                print(joke_1)
                speechtx(joke_1)
            elif "spotify" in data1:
                open_app("spotify.exe")
            elif "calculator" in data1:
                open_app("calc.exe")
            elif "exit" in data1:
                speechtx("Hope I was of help")
                break    
            time.sleep(5)
            
    else:
        print("Thanks")
        
         
        
        
         
         