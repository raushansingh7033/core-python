# First install the library if not installed:
# pip install pyttsx3

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Say something
engine.say("Hello! I am your Python text to speech assistant.")

# Run the speech
engine.runAndWait()
