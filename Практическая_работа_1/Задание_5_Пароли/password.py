import random
import string


class Password:
    def __init__(self, value):
        self.value = value

    def is_safe(self):
        return (len(self.value) >= 10
                and any(c.islower() for c in self.value)
                and any(c.isupper() for c in self.value)
                and any(c.isdigit() for c in self.value))

    def generate(self, n=12):
        chars = string.ascii_letters + string.digits
        self.value = "".join(random.choice(chars) for _ in range(n))
        while not self.is_safe():
            self.value = "".join(random.choice(chars) for _ in range(n))
        return self.value


print(Password("12345").is_safe())
print(Password("MyPassword123").is_safe())
p = Password("")
print("Новый пароль:", p.generate())