import random as r
import string
#1
L = [11, 12, 13, 14]

# i
L.extend([50, 60])
print("After adding:", L)

# ii
L.remove(11)
L.remove(13)
print("After removing:", L)

# iii
L.sort()
print("Ascending:", L)

# iv
L.sort(reverse=True)
print("Descending:", L)

# v
print("13 found?", 13 in L)

# vi
print("Count:", len(L))

# vii
print("Sum:", sum(L))

# viii
L = [12, 14, 50, 60]
odd_sum = 0
for num in L:
    remainder = num % 2
    if remainder != 0:
        odd_sum = odd_sum + num
print("Odd sum:", odd_sum)

# ix
even_sum = 0
for num in L:
    remainder = num % 2
    if remainder == 0:
        even_sum = even_sum + num
print("Even sum:", even_sum)

# x
prime_sum = 0
for num in L:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        remainder = num % i
        if remainder == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum = prime_sum + num
print("Prime sum:", prime_sum)
# xi
L.clear()
print("After clear:", L)

# xii
del L
#2
nums = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n
print("Sum:", total)
#3
nums = [1, 2, 3, 4, 5]
product = 1
for n in nums:
    product *= n
print("Product:", product)
#5
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i)
D[8] = 8.8
print(D)

# (ii)
D.pop(2)
print(D)

# (iii)
print("6 key present?", 6 in D)

# (iv)
print("Count:", len(D))

# (v)
print("Sum of values:", sum(D.values()))

# (vi)
D[3] = 7.1
print(D)

# (vii)
D.clear()
print("After clear:", D)
#6
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i)
S1.update([55, 66])
print(S1)

# (ii)
S1.discard(10)
S1.discard(30)
print(S1)

# (iii)
print("40 present?", 40 in S1)

# (iv)
print("Union:", S1 | S2)

# (v)
print("Intersection:", S1 & S2)

# (vi)
print("S1 - S2:", S1 - S2)
#7


# (i)
for _ in range(100):
    length = r.randint(6, 8)
    rand_str = ''.join(r.choice(string.ascii_letters) for _ in range(length))
    print(rand_str)

# (ii)
for n in range(600, 801):
    if is_prime(n):
        print(n, end=" ")

# (iii)
for n in range(100, 1001):
    if n % 63 == 0:
        print(n, end=" ")
#8
exam_st_date = (11, 12, 2025)

day = exam_st_date[0]
month = exam_st_date[1]
year = exam_st_date[2]

print(f"The examination will start from:{day}/{month}/{year}")
#9
nums = [10, 23, 45, 60, 77, 100]
for n in nums:
    if n % 5 == 0:
        print(n)
#10
num = 7
is_even = (num % 2 == 0)
print("Even?" if is_even else "Odd?")
#11
text = "Emma is good. Emma loves Python. Emma is smart."
count = text.count("Emma")
print("Occurrences of Emma:", count)
#12
L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]
new_list = []
for x in L1:
    if x % 2 != 0:
        new_list.append(x)
for y in L2:
    if y % 2 == 0:
        new_list.append(y)
print(new_list)
#13
positions = [(2,3), (4,5), (6,7), (7,8)]
even_positions = []
for p in positions:
    x = p[0]
    if x % 2 == 0:
        even_positions.append(p)
print(even_positions)
sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}

#14
sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
above = []
for sid, val in sensor_data.items():
    if val > 3.0:
        above.append(sid)
print(above)
#15
commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}

not_executed = commands_received - commands_executed
print("Not executed:", not_executed)