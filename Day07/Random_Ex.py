import random
from random import randint

my_count = 0
your_count = 0
drew_count = 0

iteration = 0
while iteration < 1_000:
    # print(randint(1,6))
    # input() # 무한 루프 출력에서 Enter를 눌러야 다음으로 넘어감

    my_dice = randint(1,6)
    your_dice = randint(1,6)

    print('=' * 25)
    print(f"My dice : {my_dice}")
    print(f"Your dice : {your_dice}")

    print('*' *25)
    if my_dice == your_dice:
        drew_count += 1
        print("> Drew")
    elif my_dice > your_dice:
        my_count += 1
        print("> I won")
    else:
        your_count += 1
        print("> You won")

    print('*' *25)
    print(f"My Win : {my_count}",f"\nYour Win : {your_count}",f"\ndrew : {drew_count}")
    print('=' *25)
    print()

    iteration += 1