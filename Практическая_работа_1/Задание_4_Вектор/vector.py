import math


class Vector:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        # вектор задается координатами начала (x1, y1, z1) и конца (x2, y2, z2)
        self.x = x2 - x1
        self.y = y2 - y1
        self.z = z2 - z1

    def __add__(self, o):
        # новый вектор откладываем от начала координат
        return Vector(0, 0, 0, self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Vector(0, 0, 0, self.x - o.x, self.y - o.y, self.z - o.z)

    def dot(self, o):
        return self.x * o.x + self.y * o.y + self.z * o.z

    def length(self):
        return math.sqrt(self.dot(self))

    def angle(self, o):
        return math.degrees(math.acos(self.dot(o) / (self.length() * o.length())))

    def __str__(self):
        return f"({self.x}; {self.y}; {self.z})"


a = Vector(1, 1, 1, 2, 3, 4)
b = Vector(2, 5, 0, 6, 0, 6)
print("a =", a)
print("b =", b)
print(a + b)
print(a - b)
print("Скалярное:", a.dot(b))
print("Длина a:", round(a.length(), 2))
print("Угол:", round(a.angle(b), 2))