#2. 짝수와 홀수 구분하기

def is_odd_or_even(number):
    if int(number) % 2 == 0:
        return '짝수 입니다.'
    return '홀수 입니다.'

input_number = input("입력: ")
print(is_odd_or_even(input_number))
