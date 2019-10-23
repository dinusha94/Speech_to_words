import speech_recognition as sr 
  
AUDIO_FILE = ("1.wav") 
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
    #reads the audio file. Here we use record instead of 
    #listen 
	audio = r.record(source)   
  
try: 
	txt = r.recognize_google(audio) 
	#print the number of words
	print(len(txt.split(' ')))
  
except sr.UnknownValueError: 
	print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
	print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
