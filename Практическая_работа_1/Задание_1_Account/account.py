class Account:
    def __init__(self, owner, number, percent, date, amount=0):
        self.owner = owner
        self.number = number
        self.percent = percent
        self.date = date
        self.amount = amount

    def change_owner(self, new):
        self.owner = new

    def withdraw(self, s):
        if s > self.amount:
            print("Недостаточно средств")
        else:
            self.amount -= s

    def deposit(self, s):
        self.amount += s

    def add_percent(self):
        self.amount += self.amount * self.percent / 100

    def to_dollars(self, rate=90):
        return self.amount / rate

    def __str__(self):
        return f"{self.owner}, счет {self.number}, {self.amount:.2f} руб."


a = Account("Иванов", "12345", 10, "01.09.2024", 50000)
print(a)
a.deposit(10000); print(a)
a.withdraw(20000); print(a)
a.add_percent(); print(a)
print("В долларах:", round(a.to_dollars(), 2))
a.change_owner("Петров"); print(a)