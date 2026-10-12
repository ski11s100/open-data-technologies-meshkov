import math


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        return 0


class Circle(Figure):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def resize(self, k):
        self.r *= k

    def area(self):
        return math.pi * self.r ** 2


class Rectangle(Figure):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def resize(self, k):
        self.w *= k
        self.h *= k

    def area(self):
        return self.w * self.h


class Square(Rectangle):
    def __init__(self, x, y, a):
        super().__init__(x, y, a, a)


figs = [Circle(0, 0, 5), Rectangle(1, 1, 4, 6), Square(2, 2, 3)]
for f in figs:
    f.move(1, 1)
    f.resize(2)
    print(type(f).__name__, "площадь =", round(f.area(), 2))