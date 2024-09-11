class Fruit:
    name = "오렌지"
    color = "노란색"

    def taste(self):
        print("새콤하다")

    def vitamin(self):
        print("비타민 C가 풍부하다.")

orange = Fruit()

print(f"과일명 : {orange.name}")
print(f"색상 : {orange.color}")

orange.taste()
orange.vitamin()