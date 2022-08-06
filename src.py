'''
PYTHAKON 2022

TEAM MEMBERS:
Yatharth Chauhan
Mehul Patel
Reeya Thanki

Project: Virtual Voice Assistant Using Python
'''

from click import BaseCommand
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import time
import pyjokes
import pyautogui
import os.path


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# to wish


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning Sir")
    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon Sir")
    else:
        speak(f"Good Evening Sir")
    speak("Please tell me how may I help you")


if __name__ == "__main__":  # main program
    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for tasks

        if "open visual studio code" in query:
            npath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)

        # elif 'play' in query:
        #     song = query.replace('play', '')
        # speak('playing ' + song)
        # pywhatkit.playonyt(song)

        if "open python" in query:
            npath = "D:\\New\\Yatharth Chauhan\\Downloads\\py\\python.py"
            os.startfile(npath)

        elif "open cmd" in query:
            os.system("start cmd")

        if "open file" in query:
            npath = "D:\\New\\Yatharth Chauhan\\Downloads\\py\\file.py"
            os.startfile(npath)

      #     npath = "C: \\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
      #     os.startfile(npath)
          # cm = takecommand().lower()
          # webbrowser.open(f"{cm}")

      # elif "open google" in query:
      #     speak("Sir, What Should I Search On Google")
      #     cm = takecommand().lower()
      #     webbrowser.open(f"{cm}")

    #    elif "open notepad" in query:
    #         npath = "C:\\Windows\\system32\\notepad.exe"
    #         os.startfile(npath)

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        # elif "open command prompt" in query:
        #     os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()

        # elif "play music" in query:
        #     music_dir = "E:\\music"
        #     songs = os.listdir(music_dir)

            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Sir, What Should I Search On Google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        # elif "song on youtube" in query:
        #     kit.playonyt("see you again")

        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = BaseCommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished sir')


# to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

# to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

# to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
