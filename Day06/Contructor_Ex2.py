class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_member(self):
        print(f"이름 : {self.name}, 나이 : {self.age}")

member1 = Member("홍길동", "400")
member1.show_member()

member2 = Member("파이썬", "40")
member2.show_member()