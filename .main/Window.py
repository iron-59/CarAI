from tkinter import *

class Render:
    def __init__(self):
        self.window = Tk()
        self.window.title('test')
        self.window.configure(width = 500, height = 300)
        self.window.configure(bg='white')

    def initiate(self):
        self.window.mainloop()
