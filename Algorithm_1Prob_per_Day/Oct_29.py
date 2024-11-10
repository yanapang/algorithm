import math

def get_sqrt(user_num):
    val = int(math.sqrt(user_num * 2))

    while (val * (val+1))/2 > user_num:
        val -= 1

    return val


userInput = float(input())

print(get_sqrt(userInput))