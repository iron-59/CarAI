from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.title("Car AI")

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

window.geometry(str(w)+ "x" + str(h))

def openwindow():
    window.mainloop()


class Render:
    def __init__(self, img):
        self.image = img
        return
    def run(self):
        global window, w, h
        frame = Frame(window, width = w, height = h)
        frame.pack()
        frame.place(anchor='center',relx=.5,rely=.5)

        label = Label(frame, image = self.image)
        label.pack()
class ImageCache:
    def __init__(self):
        global w, h
        self.cache = [ImageTk.PhotoImage(Image.open("C:/Users/alext/Desktop/Coding/CarAI/.images/track.png").resize((w, h)))]
    def at_index(self, num):
        return self.cache[num]



