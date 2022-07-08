from http import server
from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime
import smtplib

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
print(voice[0].id)
engine.setProperty("voice", voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning!")
    elif 12<=hour<=18:
        speak("Good after noon!")
    elif 18<hour<=24:
        speak("Good Evening")
    speak("I am Aili. Sir, how can i help you")

def takeCommand():
    """"Takes sound through Microphone as input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        speak("Your voice is being recognized")
        query = r.recognize_google(audio, language="en-ind")
        print(f"User: {query}")
    except Exception as e:
        print("voice does not recognize! Please Speak loudly")
        speak("voice does not recognize! Please Speak loudly")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sender_gmail@gmail.com", "sender_password")
    server.sendmail("sender_gmail@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if "your name" in query:
            speak("I am Aili")

        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak("According to wikipedia")
                speak(result)
            except Exception as e:
                speak(f"There is no any article found in wikipedia on {query}")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query or "play song" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            song = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[song]))

        elif "favorite music" in query or "favorite song" in query:
            music_dir = "D:\\favorite_music"
            songs = os.listdir(music_dir)
            song = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[song]))

        elif "code" in query:
            os.startfile("C:\\Users\Arjun kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\code")

        elif "open chrome" in query:
            os.startfile("C:\\Program Files\\Google\Chrome\\Application\\chrome")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif "email" in query:
            try:
                speak("what should I say!")
                content = takeCommand()
                to = "receiver_gmail@gmail.com"
                sendEmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send email")

        
