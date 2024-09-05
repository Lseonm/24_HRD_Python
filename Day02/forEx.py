for x in range(5):
    print(f"{x} : 안녕하세요!")
    
print()

for _ in range(3):  # 이렇게도 가능
    print("안녕하세요!")

print()

for x in "안녕하세요": # 이렇게도 가능
    print(f"{x} : 안녕하세요.")

print()
    
for x in ['안', "녕하", '세', 0]:
    print(f"{x} : 안녕하세요")

print()

sum = 0;
for i in [1,2,3,4,5,6,7,8,9,10]: # 복잡 -> range 함수 사용
    sum += i
print(sum)

sum = 0;
for i in range(1,101):
    sum+=i
print(sum)

print()

for i in range(10):
    print(i, end=' ')

print()

for i in range(1, 10, 2):
    print(i, end=' ')

print()

for i in range(20, 0, -2):
    print(i, end = ' ')

print()
# 1~200 수 중에 5의 배수 구하기
sum = 0

for i in range(1, 201, 5):
    sum += i
print(f"1~200까지 수 중에 5의 배수의 합 : {sum}")

# 100~300중 3의 배수
for i in range(100, 301):
    if i % 3 == 0:
        print(f"3의 배수 : {i}", end = ' ')

print()

x:str = input("영어 입력 : ")
for i in x:
    print(i)


for a in range(2,10):
    print(f"====={a}단=====")
    for b in range(1,10):
        c = a * b
        print(f"{a} X {b} = {c}")