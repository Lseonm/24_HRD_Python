class Animal(object):
    name = "고양이" # property == instance 변수

    def sound(self, name): # (self)를 0번째 매개변수라고 함 -> this (자기 자신의 소속(클래스)을 나타내는 포인터)
        self.name = name
        print(f"{name}가 소리를 낸다")


cat = Animal()
cat.sound("고양이")
