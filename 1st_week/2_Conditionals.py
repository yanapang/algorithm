#If / Else
def is_adult(age):
    if age > 20:
        print('Adult')
    else :
        print('Child')

is_adult(30)

print('========================')

#반복문
fruits = ['Apple','Pear', 'Strawberry', 'Persimmon']
for fruit in fruits:
    print(fruit)

#example 함수, 딕셔너리, 반복문, 조건문 이해완
def count_fruits(fruit_name):
    fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
    count = 0

    for f in fruits:
        if f == fruit_name:
            count += 1
    return count


print(count_fruits('사과'))
print(count_fruits('딸기'))


#example 반복문, 조건문
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def get_age(name):
    for person in people:
        if person['name'] == name:
            return person['age']
    return 'There is No Info about '+ name;

print(get_age('bob'))
print(get_age('john'))
print(get_age('bk'))


#Class - 객체화
class Person:
    def __init__(self, name): #initiation, 시작, 필수
        self.name = name
    def sayhello(self, toWhom):
        print(f"hello, {toWhom}. I am {self.name}")


rtan = Person("르탄")
rtan.sayhello("병관")