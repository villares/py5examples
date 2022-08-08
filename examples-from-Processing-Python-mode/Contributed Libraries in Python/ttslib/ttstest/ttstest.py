add_library('ttslib')


def setup():
    size(100, 100)
    smooth()
    global tts
    tts = TTS()


def draw():
    background(255)
    fill(255)
    ellipse(35, 30, 25, 35)
    ellipse(65, 30, 25, 35)
    fill(0)
    ellipse(40, 35, 10, 10)
    ellipse(60, 35, 10, 10)
    no_fill()
    arc(50, 50, 50, 50, 0, PI)


def mouse_pressed():
    tts.speak("Hi! I am a speaking Processing sketch")
