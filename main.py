import speech_recognition as sr


listener = sr.Recognizer()
try:
    with sr.Microphone() as src:
        print("Ready For Command")
        voice = listener.listen(src)
        command = listener.recognize_google(voice)
        print(command)
finally:
    pass