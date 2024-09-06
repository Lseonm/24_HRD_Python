
numbers = list(range(0,1001)) # 0 ~ 1000까지 리스트 생성 방법
print(numbers)


v = [1,2,3]

V = [[1,2,3], [4,5,6], [7,8,9]]

values1 = V[0] # scalar 타입 (리스트 타입으로 반환)

value1 = V[0][0] # get (read) 값을 가져옴 (정수형태로 값만 반환)

print(values1)
print(value1, end=' ')
print(V[0][1], end=' ')
print(V[0][2])

print()

for i in range(len(V)):
    for j in range(len(V[i])):
        scalar = V[i][j]
        print(scalar, end='\t')
    print()


animals:list = ['사자', '호랑이', '코끼리','코뿔소']
index = 0
size = len(animals)

while index < size:
    animal: str = animals[index]
    print(animal, end=' ')
    index += 1

print()

questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answers = ['a', 'u', 't', 'p']

T_Count = 0
F_Count = 0

for i in range(len(questions)):
    q = "%s 에서 밑줄(_)안에 들어갈 알파벳은?" % questions[i]

    ans = input(q)

    if ans == answers[i]:
        print("정답입니다!")
        T_Count += 1
    else :
        print("틀렸습니다!")
        F_Count += 1
print()
print(f'맞은 개수 : {T_Count}')
print(f'틀린 개수 : {F_Count}')