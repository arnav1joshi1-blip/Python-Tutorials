import math

print("Twinkle, twinkle, little star\nHow I wonder what you are\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star\nHow I wonder what you are")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name + " " + last_name)

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
print(f"Area of circle: {area} cm2")

color_list = ["Red", "Green", "White", "Black"]
print("First color:", color_list[0])
print("Last color:", color_list[-1])

n = input("Enter a number: ")
result = int(n) + int(n*2) + int(n*3)
print("Result:", result)

numbers = input("Enter comma-separated numbers: ")
num_list = numbers.split(",")
num_tuple = tuple(num_list)
print("List:", num_list)
print("Tuple:", num_tuple)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

a = input("Enter first number: ")
b = input("Enter second number: ")
a, b = b, a
print("After swapping: a =", a, "b =", b)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)

a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))
if a + b + c == 180:
    print("The angles form a triangle")
else:
    print("The angles do not form a triangle")

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
amount = p * (1 + r/100) ** t
ci = amount - p
print("Compound Interest:", ci)

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

n = int(input("Enter a number: "))
sum_squares = sum(i**2 for i in range(1, n+1))
print("Sum of squares:", sum_squares)
