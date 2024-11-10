print("hello world!")

#변수와 기본 연산
a = 3
b = 2
c = a + b
d = a / b
e = a * b
f = a - b
aaa = a + b + b
a_plus_b = a + b
a_minus_b = a - b

print (a, b, c)

name = 'bob'
age = 14
isAdult = age > 19

print(isAdult)

#List
name = ["watermelon", "apple", "pear"]

print(name[1])

#dictionary
bk = {
    "name":"kilDong Hong",
    "age":18,
    "address":"GyeonggiDo"
}

#dictionary in List
people = [
    {
        "name":"Hong KilDong",
        "age":18,
        "address":"GyeonggiDo"
    },
    {
        "name": "Kim Hana",
        "age": 25,
        "address": "Seoul"
    },
]

print(people[0]['name'])

#함수 (function)
def sum(a, b):
    return a + b;

print(sum(1,5))


