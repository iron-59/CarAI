import keyboard
class Car:

    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self):
        self.x += 1
        print(self.x)
class InputListener:
    def __init__(self, car, running):
        self.run = running
        self.car = car
    def listen(self):
        while self.run:
            if keyboard.is_pressed('w'):
                print('w')
                return
            elif keyboard.is_pressed('a'):
                print('a')
                return











