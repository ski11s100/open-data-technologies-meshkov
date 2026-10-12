class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def delivery(self):
        return 0

    def total(self):
        return self.price + self.delivery()


class Book(Product):
    def delivery(self):
        return self.weight * 50


class Tech(Product):
    def delivery(self):
        return self.weight * 100


class Food(Product):
    def delivery(self):
        return 0


class Group:
    def __init__(self):
        self.items = []

    def add(self, p):
        self.items.append(p)

    def total(self):
        return sum(p.total() for p in self.items)


g = Group()
g.add(Book("Книга", 2500, 1.2))
g.add(Tech("Микроволновка", 8990, 12.5))
g.add(Food("Кофе", 750, 0.25))
for p in g.items:
    print(p.name, p.total())
print("Итого:", g.total())