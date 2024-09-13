import random
from random import randint

iteration = 0

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0

while iteration < 10_000:
    num = randint(1,6)


    if num == 1:
        num_1 += 1
    elif num == 2:
        num_2 += 1
    elif num == 3:
        num_3 += 1
    elif num == 4:
        num_4 += 1
    elif num == 5:
        num_5 += 1
    else:
        num_6 += 1

        iteration += 1

# 수가 길어지니까 전체를 똑같은 수로 나눠서 직관적으로 보기 쉽게끔 구현
print('*' * (num_1 // 100))
print('*' * (num_2 // 100))
print('*' * (num_3 // 100))
print('*' * (num_4 // 100))
print('*' * (num_5 // 100))
print('*' * (num_6 // 100))
