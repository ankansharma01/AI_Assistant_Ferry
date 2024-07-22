import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
          engine.say(audio)
          engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<=12:
         speak("Good Morning")
  elif hour>12 and hour<=18:
         speak("good afternoon")
  else :
         speak("good evening")

  speak("i am ferry  i am your Assistant How may i help you")     

def takeCommands():
      

      r = sr.Recognizer()   
      with sr.Microphone() as source :
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source)
      try :
        print("Recognzing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n") 
      except Exception as e:
        print("Sorry!Say That Again...")   

        return "nothing found "
      return query


if __name__=="__main__":
        wishMe()
        while True:
           query = takeCommands().lower()
           
           if 'wikipedia' in query:
                  speak('searching wikipedia...')    
                  query = query.replace("wikipedia", "")
                  results = wikipedia.summary(query,sentences=2)
                  speak("According to wikipedia")
                  print(results)
                  speak(results)
           elif 'open youtube' in query:
                  webbrowser.open("youtube.com")
           elif 'open google' in query:
                  webbrowser.open("google.com")
           elif  'open stackoverflow' in query:
                  webbrowser.open("stackoverflow.com")
           elif 'the time' in query :
                  strTime=datetime.datetime.now().strftime("%H:%M:%S")   
                  speak(f"The Time is {strTime}")   
                        
                  
                  
       
    