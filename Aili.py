import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime
import smtplib

# Initilizing Aili voice
engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
print(voice[0].id)
engine.setProperty("voice", voice[1].id)

def speak(audio):
    """Use to speak  given sentences"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """According to time Aili wish me using this function"""
    hour = int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning!")
    elif 12<=hour<=18:
        speak("Good after noon!")
    elif 18<hour<=24:
        speak("Good Evening")
    speak("I am Aili. Sir, how can i help you")

def takeCommand():
    """"Takes sound through Microphone as input and return sentence as output"""
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
        speak("voice does not recognize!")
        return "None"
    return query

def sendEmail(to, content):
    """Take receiver's address and sender message as input and send Email to receiver's address"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sender_gmail@gmail.com", "sender_password")
    server.sendmail("sender_gmail@gmail.com", to, content)
    server.close()

def snakeWaterGun():
    """This is snake water gun game which is executed when play game command given"""
    print("Welcome to Snake, Water and Gun game\n")
    speak("Welcome to Snake, Water and Gun game")
    object= ["s", "w", "g"]
    x=5
    score1=0
    score2=0
    while (x>=0):
        print("""Choose any one:\nsnake\nwater\ngun\n""")
        speak("""Choose any one:snake or water or gun""")
        yourinput = takeCommand().lower()
        computer= random. choice(object)
        
        if computer=="w" and "s" in yourinput:
            print("Aili had chosen: water")
            speak("I had chosen: water")
            print("You had chosen: snake")
            speak("You had chosen: snake")
            print("You won!")
            speak("You won!")
            print("The remaining rounds:", x)
            x-=1
            score1+=100
        
        elif computer=="w" and "g" in yourinput:
            print("Aili had chosen: water")
            speak("I had chosen: water")
            print("You had chosen: gun")
            speak("You had chosen: gun")
            print("Aili won!")
            speak("I won!")
            score2+=100
            print("The remaining rounds:", x)
            x-=1
        
        elif computer=="g" and "s" in yourinput:
            print("Aili had chosen: gun")
            speak("I had chosen: gun")
            print("You had chosen: snake")
            speak("You had chosen: snake")
            print("Aili won!")
            speak("I won")
            score2+=100
            print("The remaining rounds:", x)
            x-=1
    
        elif computer=="g" and "w" in yourinput:
            print("Aili had chosen: gun")
            speak("I had chosen: gun")
            print("You had chosen: water")
            speak("You had chosen: water")
            print("You won!")
            speak("You won!")
            score1+=100
            print("The remaining rounds:", x)
            x-=1
        
        elif computer=="s" and "g" in yourinput:
            print("Aili had chosen: snake")
            speak("I had chosen: snake")
            print("You had chosen: gun")
            speak("You had chosen: gun")
            print("You won!")
            speak("You won!")
            print("The remaining rounds:", x)
            x-=1
            score1+=100
        
        elif computer=="s" and "w" in yourinput:
            print("Aili had chosen: snake")
            speak("I had chosen: snake")
            print("You had chosen: water")
            speak("You had chosen: water")
            print("I won!")
            speak("I won!")
            print("The remaining rounds:", x)
            score2+=100
            x-=1
        
        elif computer=="w" and "w" in yourinput:
            print("Aili had chosen: water")
            speak("I had chosen: water")
            print("You had chosen: water")
            speak("You had chosen: water")
            score1+=50
            score2+=50
            print("Draw!")
            speak("Draw!")
            print("The remaining rounds:", x)
            x-=1
        
        elif computer=="s" and "s" in yourinput:
            print("Aili had chosen: snake")
            speak("I had chosen: snake")
            print("You had chosen: snake")
            speak("You had chosen: snake")
            print("Draw!")
            speak("Draw!")
            score1+=50
            score2+=50
            print("The remaining rounds:", x)
            x-=1
        
        elif computer=="g" and "g" in yourinput:
            print("Aili had chosen: gun")
            speak("I had chosen: gun")
            print("You had chosen: gun")
            speak("You had chosen: gun")
            score1+=50
            score2+=50
            print("Draw!")
            speak("Draw!")
            print("The remaining rounds:", x)
            x-=1
        
        else:
            print("Speak valid word")
            speak("speak valid word")
            print("The remaining rounds:", x)
            print("Aili had chosen:", computer)
        
    print("\nYour score:       Aili's score:\n\n","  ",  
                score1, "                ", score2,"\n")
    speak(f"Your score is  {score1} and My score is {score2}")
    
    if score1>score2:
        print("Congratulation! You won the game.")
        speak("Congratulation! You won the game.")
        speak("You are really champion in this game")
        speak("Oh! no I lose the game")
    
    elif score1<score2:
        print("I won.\nTry again!")
        speak("I won the game")
        
    elif score1==score2:
        print("Draw!")
        speak("You are really champion in this game")
    print("Game Over")
            
if __name__ == "__main__":
    """Try to say play music, play favorite music, play a song, open youtube, open google, something accoring to wikipedia, open stackoverflow, """
    # wishme()
    while True:
        query = takeCommand().lower()
        if "your name" in query:
            speak("I am Aili")

        elif "quit" in query or "bye" in query:
            speak("Ok! Good bye")
            break

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

        elif "play music" in query or "play a song" in query:
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

        elif "play game" in query:
            speak("I am very excited! let's play game")
            snakeWaterGun()

        else:
            print("serching....")
            speak("Searching in google....")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("Here the result from google0...")
