# __new__ 키워드로 생성자를 만들 수 있지만 초기화가 되니까 안 씀
class Student():
    name = ""
    student_id = 0
    department = ""

    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

person = Student("홍길동", "20240911", "HRD")
print(person.name)