from tkinter import *

class Render:
    def __init__(self):
        self.window = None
        return
    def run(self):
        self.window = Tk()
        self.window.title("test")
        self.window.configure(width = 500, height = 300)
        self.window.configure(bg='lightgray')
        self.window.mainloop()
