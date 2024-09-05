value_a:int = 10
value_a:float = 10.4
print(value_a)  # 파이썬에서는 덮어쓰기가 됨


score = int(input("점수 입력 : "))
result:str = ''

if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'F'

print(f"Your grade is {result}")

