# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     print(f"{i} : {sum}")
#     i += 1
#
# print(f"총합 : {sum}")

s:str = "Python is widely used by a number of big companies"
i = 0
count = 0 # 모음 개수

while i <= len(s) - 1:
    if s[i].upper() == 'A' or s[i].upper() == 'E' or s[i].upper() == 'I' or s[i].upper() == 'O' or s[i].upper() == 'U':
        print(f"모음 : {s[i]}")
        count += 1
    i += 1

print(f'모음의 갯수 : {count}')