from gtts import gTTS
from playsound import playsound
k=str(input("please wite the text here: "))
audio="speech.mp3"
language="en"
sp=gTTS(text=k,lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("audio is played successfully")