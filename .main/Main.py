from Car import *
from Render import *

running = True
x = 0
render = Render()
def run():
    global running, x, render

    render.run()
    while running:


        print('test')
        if x >= 5:
            running = False
        x += 1
run()






