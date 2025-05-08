TransientStorage = []
Diary = {}
num1 = 0

while True:
    num1 = input("전화번호를 입력하시겠습니까? : Y(1번) , N(2번)")
    if num1 == "1" or num1 == "Y" or num1 == "y":
        Name = input("이름을 입력하세요 : ")
        PhonNumber = int(input("전화번호를 입력하세요:"))
        Diary.append(Name)
