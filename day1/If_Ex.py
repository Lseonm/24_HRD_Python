score = int(input("점수 입력 : "))
if score >= 80 :
    print("합격")
else :
    print("불합격")
    
    
age = int(input("나이 입력 : "))
if age >= 65 :
    print("입장료 무료")

id = int(input("주민번호 앞자리 입력 : "))
if (id == 1) | (id == 3):
    print("남성")
    

user_pw = input("비밀번호 : ")
password = "password1234"
if user_pw == password :
    print("로그인 성공")
else :
    print("로그인 실패")
    