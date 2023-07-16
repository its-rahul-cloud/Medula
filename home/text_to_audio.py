def genrate_audio(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.save_to_file(text, 'speech.mp3')

    #engine.say(text)



