class Circle:
    radius = 10
    def getArea(self):
        area = 3.141592 * self.radius ** 2
        return area

    def getCircum(self):
        circum = 2 * 3.141592 * self.radius
        return circum


cir = Circle()

print(f"반지름 : {cir.radius}")
print(f"원의 면적 : {cir.getArea()}")
print(f"원주의 길이 : {cir.getCircum()}")