
numbers = [[10, 20, 30], [40, 50, 60, 70, 80]]

print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])

print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

print()

numbers = [[10, 20, 30], [40, 50, 60, 70, 80], [90,100,110], [120]]

print(f'numbers의 길이 : {len(numbers)}')

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end='\t')
    print()