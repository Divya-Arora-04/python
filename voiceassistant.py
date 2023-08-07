import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understanding")
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate') 
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
if __name__ == "__main__" :
   #if sptext().lower() == " hey krishna":
   while True:
        data1=sptext()
        if "your name" in data1:
            name="my name is krishna"
            speechtx(name)
        elif "old are you" in data1:
            age= " I am 20 years old" 
            speechtx(age) 
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "engineering college" in data1:
            webbrowser.open("https://www.jmit.ac.in/")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="all")
            print(joke_1)
            speechtx(joke_1)
        elif "sing a song" in data1:
            webbrowser.open("https://www.youtube.com/watch?v=v0T4NovMaTQ")
        elif "exit" in data1:
            speechtx("thankyou")
            break
        
  #  else:
       # print("thankyouu")
    
        
        
    
    
    
     