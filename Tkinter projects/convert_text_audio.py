from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = 'en'
speech = gTTS(text="Hi Teja kiran, Your project is working",lang=language,slow=False)
speech.save(audio)
playsound(audio)
print("======= audio is playing======")