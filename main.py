from matplotlib.pyplot import text
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify

#sintese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def evaluate(text):
#Reconhecer entidade do texto 
   entity = classify(text)           
        
   if entity == 'time\getTime':
        speak(core.SystemInfom.get_time())

   elif entity == 'time\getDate':
        speak(core.SystemInfom.get_date())

   elif entity == 'open\notepad':
       speak('Abrindo o bloco de notas')
       os.system('notepad.exe')
   print(text)



model = Model("model")
rec = KaldiRecognizer(model,16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True,frames_per_buffer=2048 )
stream.start_stream()

while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
       result = rec.Result()
       result = json.loads(result)
       
       if result is not None:
          text = result['text']
          evaluate(text)

          
       


