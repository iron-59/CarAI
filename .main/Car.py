from Render import *
class Car:

    def __init__(self, render):
        self.x = 0
        self.y = 0
        self.render = render
        self.render.create_moveable_img()
    def move_car(self, key_list):

        for c in key_list:
            if c == 'w':
                self.y += 100
            elif c == 'a':
                self.x -= 100
            elif c == 's':
                self.y -= 100
            elif c == 'd':
                self.x += 100
            self.render.move_img(self.x, self.y)
        print("(" + str(self.x) + "," + str(self.y) + ")")
