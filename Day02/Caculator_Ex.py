print('=' *50)
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
print('=' *50)

num = input("계산기 기능을 선택하세요.(1/2/3/4)\n> ")

num1 = int(input("첫 번째 숫자를 입력하세요 > "))
num2 = int(input("두 번째 숫자를 입력하세요 > "))


if num == '1':
    result = num1 + num2
elif num == '2':
    result = num1 - num2
elif num == '3':
    result = num1 * num2
elif num == '4':
    result = num1 / num2

print(f"결과 : {result}")