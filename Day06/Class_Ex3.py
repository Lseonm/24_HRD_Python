class Student(object):
    __name = "황재호" # 멤버 변수, 인스턴스 변수, property, 속성
    # 변수 앞에 __ 를 쓰면 private 속성이 됨

    __kor = 80
    __Eng = 90
    __math = 100

    def get_sum(self):
        sum = self.__kor + self.__Eng + self.__math
        return sum

student = Student()
print(f"총합 : {student.get_sum()}")