##아스키 코드 다루기
import string

# 1. 알파벳을 바로 꺼내오는 방법
print(string.ascii_lowercase)

# 2. ord 연산
print(ord('a'), ord('A'), ord('@'))  # 97 65 64

# 3. range
for i in range(10):
    print(i)