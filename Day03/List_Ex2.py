
colors:list = ['black', 'white', 'red', 'blue']

print(colors[0])

colors[0] = 'yellow' # set (write) => 대체 시킴
colors.append(['pink','cyan']) # 리스트안에 리스트 형태도 들어감

print(colors[:])

for i in colors:
    print(i, end=" ")

