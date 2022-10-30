from tkinter import *
from PIL import ImageTk, Image
class Render:
    def __init__(self, window, w, h, img):
        self.image = img
        self.window = window
        self.w = w
        self.h = h
        self.canvas = Canvas(window, width=w, height=h)
        self.canvas.pack()

    def background(self):
        frame = Frame(self.window, width = self.w, height = self.h)
        frame.pack()
        frame.place(anchor='center',relx=.5,rely=.5)

        label = Label(frame, image = self.image)
        label.pack()
    def create_moveable_img(self):
        self.canvas.create_image(self.w / 2, self.h / 2, anchor=None, image=self.image)
    def move_img(self, x, y):
        self.canvas.move(self.image, x, y)