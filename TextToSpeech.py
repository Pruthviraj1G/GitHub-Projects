import pyttsx3

speaker = pyttsx3.init()
text = input("Enter Your Text You Want Me To Pronounce : ")
speaker.say(text)
speaker.runAndWait()