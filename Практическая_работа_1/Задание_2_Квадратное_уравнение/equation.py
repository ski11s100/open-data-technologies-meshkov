import math


class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            return "корней нет"
        if d == 0:
            return -self.b / (2 * self.a)
        x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
        x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        return x1, x2


print(Equation(1, -5, 6).solve())
print(Equation(1, -4, 4).solve())
print(Equation(2, 1, 5).solve())