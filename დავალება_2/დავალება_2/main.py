import json

"""
#1
#შექმენით ფუნცია რომელსაც გადაეცემა list ტიპის მონაცემი და დააბრუნებს შებრუნებულ მონაცემს თითო ელემენტის გამოტოვებით


def skiping_reverse(data):
    reversed = []
    for i in range(len(data) - 1, -1, -1):
        omitted = data[:i] + data[i + 1:]
        reversed.append(omitted)
    return reversed

list = [1, 2, 3]
result = skiping_reverse(list)
print(result)

"""

"""
#2
#დაწერეთ ფუნქცია რომელიც დააბრუნებს ლისთში არსებული მონაცემების უდიდეს და უმცირეს ელემენტს


def find_MaxMin(data):
    max = data[0]
    min = data[0]

    for el in data:
        if el > max:
            max = el
        elif el < min:
            min = el
    return max, min

list = [4,7,1]
max, min = find_MaxMin(list)
print(f"max is-> {max}")
print(f"min is-> {min}")
"""

"""
#3
#შექმენით ფუნცქია რომელსაც გადაეცემა list, მისი თითოეული ელემენტი აქციეთ ტექსტურ მონაცემად და დააბრუნეთ ერთიანი ტექსტი

def list_toStr(listInput):
    text_list = [str(el) for el in listInput]
    text_result = ''.join(text_list)
    return text_result

my_list = [False, 3, 5.78, 'hi']
result = list_toStr(my_list)
print(result)
"""

"""
#4
#შექმენით ფუნცქია რომელსაც გადაეცემა ორი set მონაცემი, დააბრუნეთ საერთო ელემეტების ახალი სეტი და ასევე გაერთიანებული სეტი


def func(set_1, set_2):
    commons = set_1.intersection(set_2)
    combined = set_1.union(set_2)

    return commons, combined

first = {1,2,3}
second = {2,3,4}

commons, combined = func(first, second)

print("saerTo-> ", commons)
print("gaerTianebuli-> ", combined)

"""

"""
#5
#შექმენით ფუნცქია რომელსაც გადაეცემა ტექსტი, დაყავით ტექსტი წინადადებების მიხედვით და თითოეული 
#წინადადება დაამატეთ ლისთში რომელიც იქნება ფუნქციის დასაბრუნებელი მნიშვნელობა


import re

def func(text):
    sentence = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentence

input = "შექმენით ფუნცქია რომელსაც გადაეცემა ტექსტი. დაყავით ტექსტი წინადადებების მიხედვით!"
result = func(input)
print(result)

"""

"""
#6
#დაწერეთ ფუნქცია რომელიც აერთიანებს ორ dict ტიპის მონაცემს

def combine(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

dict1 = {'a': 1, 'b': 1, 'c': 1}
dict2 = {'b': 1, 'c': 1, 'd': 1}

print(combine(dict1, dict2))

"""

"""
#7+8
#დაწერეთ ფუნქცია რომელსაც გადაეცემა ტექსტი, შექმენით dict ტიპის მონაცემი სადაც თითოეული ასო ბგერისა 
#და სიმბოლოს რაოდენობას ჩაწერს. 
#წინა დავალებაში მიღებული მონაცემი ჩაწერეთ json ტიპის ფაილში

def func(text):
    count = {}
    for char in text:
        if char.isalpha():
            count['letters'] = count.get('letters', 0) + 1
        else:
            count['symbols'] = count.get('symbols', 0) + 1
    return count

text = "yjtr6u73tetegd2345"
res = func(text)

with open('func.json', 'w') as json_file:
    json.dump(res, json_file)

"""




