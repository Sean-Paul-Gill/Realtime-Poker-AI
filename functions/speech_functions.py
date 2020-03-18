import speech_recognition as sr

# Initializing the recognizer class

def speech_to_text():
    r = sr.Recognizer()
    # Listening to statement
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
    try:
        print("Speech deciphered as: ", end="")
        text = r.recognize_google(audio, language='en-IE')
        print(text)
        return text
    except:
        print("Speech not recognized, try again..")
        return speech_to_text()

