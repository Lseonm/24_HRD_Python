(x,y,z) = (10,20,30) # tuple

X1: tuple = (10,20,30) # tuple
X2: list = [10,20,30] # list


menu: tuple = ('짜장면','우동','짬뽕','볶음밥')

print(menu)
print(menu[:3])
print(menu[0])
print(menu[2])

# menu[0] = '탕수육' # tuple에선 지원안함 -> 수정이 불가해서
print()


# 튜플 합치기
tup1 = (10,20,30)
tup2 = (40,50,60)

tup3 = tup1 + tup2

print(tup3)
print(len(tup3))

element:tuple = (1,)
print(type(element))