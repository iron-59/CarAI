from tkinter import *
from PIL import ImageTk, Image
from Render import *
from Car import *
from Listener import KeyLogger



window = Tk()

window.title("Car AI")

window.configure(bg='')

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry(str(w)+ "x" + str(h))

cache = [ImageTk.PhotoImage(Image.open("C:/Users/alext/Desktop/Coding/CarAI/.images/track.png").resize((w, h))), ImageTk.PhotoImage(Image.open("C:/Users/alext/Desktop/Coding/CarAI/.images/car.png"))]

car = Car(Render(window, w, h, cache[1]))

def run():
    # bg_render = Render(window, w, h, cache[0])
    # bg_render.background()

    tracker = KeyLogger(window, car)

    window.bind_all('<KeyPress>', tracker.key_down)
    window.bind_all('<KeyRelease>', tracker.key_up)

    window.mainloop()



run()






