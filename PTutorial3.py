import math as m
#1
def diff_17(n):
    if n > 17:
        print(2 * abs(n - 17))
    else:
        print(17 - n)

#2
def test_range(n):
    if (100 <= n <= 1000) or (n == 2000):
        print(True)
    else:
        print(False)

#3
def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    print(result)

#4
def count_case(s):
    counts = {"UPPER": 0, "LOWER": 0}
    for ch in s:
        if ch.isupper():
            counts["UPPER"] += 1
        elif ch.islower():
            counts["LOWER"] += 1
    print(counts)

#5
def distinct_list(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    print(new_list)

#6
def even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    print(evens)

#7
def robot():
    def move():
        print("Robot is moving")
    move()

#8
def student(name, age, course):
    print(student.__code__.co_varnames[:student.__code__.co_argcount])

#9
def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    print((x, y))

#10
def classify_temperature(temp):
    if temp < 15:
        print("Cold")
    elif 15 <= temp <= 30:
        print("Moderate")
    else:
        print("Hot")

#11
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    if (x, y) == (2, 0):
        print(True)
    else:
        print(False)

#12
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Class:", self.student_class)

#13
class Student2:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

student1 = Student2(1, "A", "CSE")
student2 = Student2(2, "B", "ECE")

print("Student1:", vars(student1))
print("Student2:", vars(student2))

#14
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(m.pi * (self.radius ** 2))
    def perimeter(self):
        print(2 * m.pi * self.radius)

#15
class StringClass:
    def get_String(self):
        self.s = input("Enter a string: ")
    def print_String(self):
        print(self.s.upper())

#16
class Robot:
    def __init__(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        if self.battery_level >= 10:
            print(f"{self.name} is performing {self.task}")
            self.battery_level -= 10
        else:
            print(f"{self.name} has low battery. Please recharge.")

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is recharged.")

    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")
