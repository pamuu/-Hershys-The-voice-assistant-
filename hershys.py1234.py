import pyttsx3 
import speech_recognition as sr
import datetime
import screen_brightness_control as src
import wikipedia 
import webbrowser
import os
import smtplib
import requests
                                                                                        
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
            

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("i am hershys sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 1.0
        audio = r.listen(source)

    try:
        print("Recognizing...")      
        query = r.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n")  
  
    except Exception as e:     
        print("Say that again please...")
        return "None"  
    return query  
  
def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login()
    server.sendmail('pamusainagaharshavardhan1234@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
            speak("please enter password to access hershys")
            Name = input("Enter ur  Password sir : ")
            if Name == 'd':
                speak(' Welcome  harsha....., Please tell me how may I help you,i think you may feel better comfort with me,with all my service that i can accompany with you harshavardhan')
                while True:
                        query = takeCommand().lower()
                        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                        if 'wikipedia' in query:
                            speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                        elif 'open youtube' in query:
                            webbrowser.open("youtube.com")

                        elif 'open google' in query:
                            webbrowser.open("google.com")

                        elif 'open stackoverflow' in query:
                            webbrowser.open("stackoverflow.com")

                        elif 'play music' in query:
                            music_dir = 'C:\\Users\\adith\\OneDrive\\Desktop\\music'
                            songs = os.listdir(music_dir)
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))

                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"Sir, the time is {strTime}")

                        elif 'open code' in query:
                            codePath = "C:\\Users\\adith\\AppData\\Local\\Programs\\Microsoft VS code\\code.exe"
                            os.startfile(codePath)

                        elif 'stop' in query:
                            break

                        elif 'send email' in query:
                            try:
                                speak("What should I say?")
                                content = takeCommand()
                                contacts = {"Aditya":"pamusainagaharshavardhan12342gmail.com","sudeep":"pamusainagaharshavardhan12342gmail.com","gayathri":"gayathrigarine@gmail.com","daith":"daithkumarnaik@gmail.com","alekhya":"sriramojualekhya1@gmail.com","sudha":"saisrisudha1999@gmail.com","sri teja":"sritejaavadutha99@gmail.com", "asif sir":"asif_eee@reddif.com","Thulasi":"tulasisurisetty6@gmail.com"}
                                for i in contacts:
                                    if i in query:
                                        to = contacts[i]
                                sendEmail(to, content)
                                speak("Email has been sent!")
                            except Exception as e:
                                print(e)
                                speak("Sorry my friend. I am not able to send this email")



                        elif 'day brightness' in query:
                            src.fade_brightness(0)
                            src.fade_brightness(95, start=0)
                            speak("Brightness is adjusted  , enjoy the day screen light master")

                        elif 'night brightness' in query:
                            src.fade_brightness(0)
                            src.fade_brightness(25, start=0)
                            speak("Brightness is adjusted , Take care,yourself master")

                        elif 'number' in query:
                            speak("enter number master")
                            number=input('enter number')
                            from phonenumbers import geocoder
                            ch_number = phonenumbers.parse(number, "CH")
                            i=geocoder.description_for_number(ch_number, "en")
                            print(i)
                            speak("country"+i)
                            from phonenumbers import carrier
                            service_number = phonenumbers.parse(number, "RO")
                            j=carrier.name_for_number(service_number, "en")
                            print(j)
                            speak("sim "+j)


                        elif 'current location' in query:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            city = data['city']
                            location = data['loc'].split(',')
                            latitude = location[0]
                            longitude = location[1]
                            print("Latitude : ", latitude)
                            speak("Latitude" + latitude)
                            print("Longitude : ", longitude)
                            speak("Longitude" + longitude)
                            print("City : ", city)
                            speak("City" + city)
                            speak("city" - city)
                            speak("contact",number)