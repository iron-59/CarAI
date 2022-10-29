from Car import *
from Window import *
import os

cache = ImageCache()
render = Render(cache.at_index(0))

car = Car()

def run():
    global render, car
    listener = InputListener(car, True)
    listener.listen()
    render.run()
    openwindow()

run()






