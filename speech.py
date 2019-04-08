import speech_recognition as sr
import pyaudio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Your said : {}".format(text))

    except:
        print("Sorry could not recognize what you said!!! ")
