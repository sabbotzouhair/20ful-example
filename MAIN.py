from gradio_client import Client
import pyttsx3

#python API for the main Model MoonDream
client = Client("vikhyatk/moondream2")
result = client.predict(
		"im1.jpg",	# filepath  in 'Upload an Image' Image component
		"I'am driving and this is my frontal camera of the car, assist me by highlighting areas of potential concern. one sentence response.",	# str  in 'Input' Textbox component
		api_name="/answer_question"
						)
print(result)

#the text to speech model for the model 
engine = pyttsx3.init() # object creation

""" RATE"""
engine.setProperty('rate', 180)     # setting up new voice rate
"""VOLUME"""
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[2].id)


engine.say('Pay attention , ' + str(result))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
#engine.save_to_file('Hello World', 'COUCOU.mp3')
engine.runAndWait()