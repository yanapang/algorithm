# 문자열 팰린드롬 여부 확인

def isPalindrome(input_str):
    half = int(len(input_str) / 2)

    for i in range(half):
        if input_str[i] != input_str[-i-1]:
            return False
    return True

print(isPalindrome('radar'))
print(isPalindrome('python'))