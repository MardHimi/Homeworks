from math import sqrt
from random import randint

"""
#დაბეჭდეთ 1-და 10-მდე რიცხვების ჯამი.

sumOfNums = 0
for i in range(1, 11):
    sumOfNums += i
print("1-დან 10-მდე რიცხვების ჯამი -> ",sumOfNums)

"""

"""
#შეამოწმეთ შეყვანილი რიცხვი ლუწია თუ კენტი

number = int(input("შეიყვანეთ რიცხვი -> "))

if number % 2 == 1:
    print(f"{number} კენტია")
else:
    print(f"{number} ლუწია")
"""
"""
#გამოიანგარიშეთ შეყვანილი რიცხვის ფაქტორიალი (ფაქტორიალი - 1-დან N-მდე რიცხვების ნამრავლი)

number = int(input("შეიყვანეთ რიცხვი -> "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}-ის ფაქტორიალი არის -> {factorial}")
"""
"""
#დაბეჭდეთ 3-ის პირველი 5 ჯერადი.
for i in range(1, 6):
    numbers = i * 3
    print(numbers)
"""
"""
#გამოიანგარიშეთ სამი რიცხვის საშუალო
num_1 = float(input("შეიყვანეთ 1 რიცხვი -> "))
num_2 = float(input("შეიყვანეთ 2 რიცხვი -> "))
num_3 = float(input("შეიყვანეთ 3 რიცხვი -> "))
average = (num_1 + num_2 + num_3) / 3
print("რიცხვების საშუალო -> ", average)
"""

"""
#დააბეჭდეთ შემდეგი პატერნი:
#1
#22
#333
#4444
#55555

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
"""
"""
#დაბეჭდეთ შეყვანილი რიცხვის ციფრების ჯამი
num = int(input("Enter a number: "))

sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print("Sum of the digits:", sum_of_digits)
"""

"""
#დაბეჭდეთ სამი შეყვანილი რიცხვიდან მაქსიმალურის მნიშვნელობა

num_1 = float(input("Enter 1st number-> "))
num_2 = float(input("Enter 2nd number-> "))
num_3 = float(input("Enter 3rd number-> "))

if num_1 >= num_2 and num_1 >= num_3:
    max_number = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    max_number = num_2
else:
    max_number = num_3

print("Maximum is-> ", max_number)
"""


"""
#დაითვალეთ ხმოვანთა რაოდენობა შეყვანილ სტრიქონში.

count = 0
xmovnebi = "aeiouAEIOU"
string_in = input("enter string-> ")

for char in string_in:
    if char in xmovnebi:
        count += 1

print(f"xmovnebis raodenoba-> {count}")

"""


"""
#დაბეჭდეთ საერთო ელემენტები ორ სიას შორის.
#list1 = [1, 2, 3, 4, 5]
#list2 = [3, 4, 5, 6, 7]

common = []
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

for el in list1:
    if el in list2:
        common.append(el)

print("common elements are->", common)

"""





"""
#შექმენით შემთხვევითი რიცხვი 1-დან 10-მდე და  შეამოწმეთ დაემთხვევა თუ არა მომხმარებლის შეტანილ რიცხვს, გამოიყენეთ random ბილბლიოთეკა

random_num = randint(1, 10)

while True:
    user_input = int(input("enter number from 1 to 10-> "))

    if user_input == random_num:
        print("it's correct number")
        break
    else:
        print("Try again")

"""