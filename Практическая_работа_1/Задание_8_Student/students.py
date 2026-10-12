import json


class Student:
    def __init__(self, id, fam, name, otch, year, addr, phone, fac, course, group, ball):
        self.id = id
        self.fam = fam
        self.name = name
        self.otch = otch
        self.year = year
        self.addr = addr
        self.phone = phone
        self.fac = fac
        self.course = course
        self.group = group
        self.ball = ball

    def stipend(self):
        if self.ball < 3:
            return 0
        if self.ball >= 4.8:
            return 4000
        if self.ball >= 4:
            return 3000
        return 2000

    def __str__(self):
        return (f"{self.fam} {self.name} {self.otch}, {self.fac}, "
                f"{self.course} курс, гр.{self.group}, балл {self.ball}, "
                f"стип. {self.stipend()}")


students = [
    Student(1, "Мешков", "Егор", "Константинович", 2005, "Липецк", "111", "ИТ", 3, "Д-Э 18-24", 4.9),
    Student(2, "Иванов", "Иван", "Иванович", 2004, "Москва", "222", "ИТ", 3, "Д-Э 18-24", 4.2),
    Student(3, "Петрова", "Анна", "Сергеевна", 2006, "Тула", "333", "ИТ", 2, "Д-Э 11-25", 3.6),
    Student(4, "Сидоров", "Павел", "Олегович", 2003, "Рязань", "444", "Эконом", 4, "Э-15-23", 2.9),
]

print("a) факультет ИТ:")
for s in students:
    if s.fac == "ИТ":
        print(" ", s)

print("b) по факультетам и курсам:")
for fac in sorted(set(s.fac for s in students)):
    for course in sorted(set(s.course for s in students if s.fac == fac)):
        print(f"  {fac}, курс {course}:")
        for s in students:
            if s.fac == fac and s.course == course:
                print("   ", s.fam)

print("c) родились после 2004:")
for s in students:
    if s.year > 2004:
        print(" ", s)

print("d) группа Д-Э 18-24:")
for s in students:
    if s.group == "Д-Э 18-24":
        print(" ", s)

with open("students.json", "w", encoding="utf-8") as f:
    json.dump([s.__dict__ for s in students], f, ensure_ascii=False, indent=2)

with open("students.json", encoding="utf-8") as f:
    data = json.load(f)
new = [Student(**d) for d in data]
print("Загружено:", len(new))
print(new[0])