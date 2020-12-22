import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

#sapi5 : microsoft providing voices

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >0 and hour < 12:
        speak("good morning (UserName)")
    elif hour >=12 and hour < 18:
        speak("good afternoon (UserName)")
    else:
        speak("good evening (UserName)")

    speak("Hai (UserName) iam jarvis! how may i help you sir")

def takecammand():
    ''' it takes the input from user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listnening...")
        r.pause_thresold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        quary = r.recognize_google(audio, language ='en-in')
        print(f"user said:{quary}\n")
    except Exception as e:
        print(e)
        print("soory! say that again please")
        return "None"
    return quary

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
if __name__ == '__main__':
    wishme()
    while True:

        quary = takecammand().lower()
        # logic for ececuting the tasks based on quary
        if 'wikipedia' in quary:
            speak("searching wikipedia...")
            quary = quary.replace("wikipedia","")
            result = wikipedia.summary(quary,sentances=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in quary:
            webbrowser.open("youtube.com")
        elif 'open google' in quary:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in quary:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in quary:
             webbrowser.open("spotify.com")

        elif 'the time' in quary:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {startTime}")
        elif 'open code' in quary:
            codePath = "Your Any Platform paths"
            os.startfile(codePath)

        elif 'send email' in quary:
            try:
                speak("what should i say?")
                content = takecammand()
                to = 'You E-mail account'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend .i am not able to sned")
