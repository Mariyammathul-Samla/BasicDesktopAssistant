import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi. I am Jarvis. How can I help you?")

def takeCommand():
    '''Takes input from user voice and returns string as output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_sphinx(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)    
        print("Please repeat again...")  
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password') 
    server.sendmail('me@gmail.com', to, content)
    server.close()



if __name__ =="__main__":
    WishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir='C:\\MyMusics'
            songs=os.listdir(music_dir)
            # print(songs,"\n")
            x=random.randint(0,26)
            print("playing song",x+1)
            os.startfile(os.path.join(music_dir,songs[x]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\marya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="me@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent sucessfully")
            except Exception as e:
                speak("Sorry, I am not able to send this email at the moment. Please try again later")


        
