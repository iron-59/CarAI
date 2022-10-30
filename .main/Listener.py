from tkinter import *
from Car import *

class KeyLogger:
    down = False
    last_key = "none"
    key_change = down
    key_list = {}

    def __init__(self, window, car):

        self.window = window
        self.car = car
        self.timerhandle = window.after(20, self.timer)
    def key_down(self, event):

        if not event.char in self.key_list:
            self.key_list[event.char] = "down"
        self.down = True
        self.last_key = event.char

    def key_up(self, event):

        if event.char in self.key_list:
            self.key_list.pop(event.char)

        if len(self.key_list) == 0:
            self.down = False

    #onTimer is present to show keyboard action as it happens.
    #It is not needed to track the key changes, and it can be
    #removed.
    def timer(self):
        if self.down != self.key_change:
            self.key_change = self.down
            if self.down:
                self.car.move_car(self.key_list)

            else:
                print("Key up, last key pressed - " + self.last_key)
        self.timerhandle = self.window.after(20,self.timer)