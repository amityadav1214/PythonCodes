# importing the pyttsx library for text to speech
import pyttsx3
  
engine = pyttsx3.init()
  
l1 = ["Amit","Sameer","Shiv"]

for list in l1:
    engine.say(f"Shoutout to {list}")
    engine.runAndWait()
