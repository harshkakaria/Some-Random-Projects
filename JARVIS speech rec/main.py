import datetime
import os
import random
import webbrowser
from time import sleep as pause

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def dish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning sir , How may i help you?")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir , How may i help you?")
    else:
        speak("Good evening sir , How may i help you")

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Initializing commands")
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:
        speak("Network error..")
        return "none"
    return text

if __name__ == "__main__":
    dish()
    while True:
        IDK = takecom().lower()

        if "wikipedia" in IDK:
            speak("searching details....Wait")
            IDK.replace("wikipedia","")
            results = wikipedia.summary(IDK,sentences=3)
            print(results)
            speak(results)

        elif "tell me a joke" in IDK:
            a = pyjokes.get_joke()
            speak(a)
            print(a)

        elif "play on youtube" in IDK:
            a = str(input("enter the vid to be played :"))
            pywhatkit.playonyt(a)

        elif 'open youtube' in IDK or "play a vid" in IDK:
            webbrowser.open("https://www.youtube.com/channel/UCNTUEU3PrB4QkpD2NsnD9HQ?view_as=subscriber")
            speak("opening youtube")

        elif 'open github' in IDK:
            webbrowser.open("https://www.github.com/harshkakaria")
            speak("opening github")

        elif 'open instagram' in IDK:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open google' in IDK:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open yahoo' in IDK:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in IDK:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'good bye' in IDK:
            speak("good bye")
            exit()

        elif "normal shutdown" in IDK:
            speak("shutting down")
            os.system("shutdown -s")

        elif "who are you" in IDK or "about you" in IDK or "your details" in IDK:
            about = "im an AI that can control your computer and help you in many things"
            speak(about)

        elif "hello" in IDK or "hello Jarvis" in IDK:
            hel = "Hello  Sir ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "your name" in IDK or "sweat name" in IDK:
            na_me = "Jarvis"
            print(na_me)
            speak(na_me)

        elif IDK == 'none':
            continue
        elif 'exit' in IDK or 'abort' in IDK or 'bye' in IDK or 'quit' in IDK or "shut up" in IDK:
            ex_exit = 'Thank you sir'
            speak(ex_exit)
            exit()

        elif "open ebay" in IDK:
            speak("opening ebay")
            webbrowser.open("https://ebay.com")

        elif "open flipkart" in IDK:
            speak("opening facebook")
            webbrowser.open("https://flipkart.com")

        elif "open roblox" in IDK:
            speak("opening RBX")
            webbrowser.open("https://roblox.com/home")

        else:
            speak("srry sir cant understad you please reapeat?")
