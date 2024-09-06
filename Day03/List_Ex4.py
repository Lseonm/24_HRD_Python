Flowers = ['할미꽃', '무궁화', '장미', 'ilis',]
print(Flowers)
Flowers.append('벚꽃')
print(Flowers)
# Flowers.clear() # 전체 삭제
# print(Flowers)
Flowers.sort() # 정렬
print(Flowers)
Flowers.reverse()
print(Flowers)


# 리스트 추가하는 또 다른 방법
flower = ['물망초']
new_flowers = Flowers + list(flower)
print(new_flowers)

Flowers.clear()
print(Flowers)

print()

scores = []
sum = 0
avg = 0

while True:
    score = int(input("성적을 입력하세요(종료 시 -1 입력) > "))

    if score == -1:
        break
    else:
        scores.append(score)
        sum += score

avg = sum / len(scores)

print(f'점수 : {scores}')
print(f'합계 : {sum}')
print(f'평균 : {avg}')