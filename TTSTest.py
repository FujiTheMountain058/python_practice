import pyttsx3 as ts

def slower():
    engine = ts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 100)
    print("""
       
This is a slow message
       
    """)
    engine.say("This is a slow message")
    engine.runAndWait()
    
def faster():
    engine = ts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 290)
    print("""
       
This is a fast message
       
    """)
    engine.say("This is a fast message")
    engine.runAndWait()

def volume():
    engine = ts.init()
    engine.getProperty('volume')
    engine.setProperty('volume', .5)
    print("""
    
This is a message in 0.5 volume
    
    """)
    engine.say("This is a message in 0.5 volume.")
    engine.runAndWait()
    

slower()
faster()
volume()