class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, o):
        return Complex(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return Complex(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return Complex(self.re * o.re - self.im * o.im,
                       self.re * o.im + self.im * o.re)

    def __str__(self):
        if self.im < 0:
            return f"{self.re} - {-self.im}i"
        return f"{self.re} + {self.im}i"


z1 = Complex(3, 4)
z2 = Complex(1, -2)
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)