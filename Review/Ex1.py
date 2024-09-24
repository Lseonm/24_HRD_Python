# number = input("정수 입력 : ")
# last_character = number[-1]
#
# if last_character in "02458":
#     print("짝수")
# if last_character in "13579":
#     print("홀수")
#
#
#
# num = int(input("정수 입력 : "))
# if num > 0:
#     raise NameError
# else:
#     print("음수")

# values = [1, 2, 3, 4, 5]
# values.insert(0, 0)
# print(values)

# number = [1,2,3,4,5,6,7,8,9,10]
# number = list(range(100)) # 0~100 까지 들어있음

# number = [_ for _ in range(100)]

# number = []
# for i in range(100):
#     number.append(i)
#
# print(number)

# 네트워크에서 시스템으로 값이 들어옴 (0은 오류값임)
list_values = [1,0,1,0,1,0,1,1,1,1]
error = 0

while error in list_values:
    list_values.remove(error)

print(list_values)

scores = [10,20,30,40,50]
sum = 0

for element in scores:
    sum += element

print(f"총합 : {sum}")


list_a = [1,2,3,4,5,6,7]
reversed_list_a = reversed(list_a)
list_a.reverse()
print(list_a)
print(reversed_list_a)

for elemnet in reversed_list_a:
    print(elemnet, end="  ")