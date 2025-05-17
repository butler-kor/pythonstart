#def 함수를 사용하여 구구단 만들기
from win32process import LIST_MODULES_32BIT
from zstandard.backend_cffi import STRATEGY_BTLAZY2


# def gugudan(x,y):
#     result = x * y
#     return result
#
# num1 = int(input("첫번째 숫자를 입력하세요:"))
# num2 = int(input("두번째 숫자를 입력하세요:"))
#
# print(f"{num1} X {num2} = ",(gugudan(num1,num2)),"입니다.")

# def 함수에 슬라이싱을 사용하여 문자열을 더하고 역순으로 출력
# def Reverse(Str1, Str2):
#     Str3 = Str1 + Str2
#     return Str3[ : : -1]
#
# str1 = input("첫번째 하고 싶은 말을 적으세요:")
# str2 = input("두번째 하고 싶은 말을 적으세요:")
# print(Reverse(str1,str2))

#def를 이용하여 성적리스트를 받고 평균 값을 출력
def Score(no1,no2,no3):
   result1 = sum(no1) / len(no1)
   result2 = sum(no2) / len(no2)
   result3 = sum(no3) / len(no3)
   return result1,result2,result3

List1 = ['수학','영어','과학','물리']
List2 = []
num1 = 0
num2 = 0
num3 = 0
no1Student = []
no2Student = []
no3Student = []
for i in range(1,4):
    num2 = num2 + 1
    List2 = []
    print(f"{num2}번째 학생의 점수를 입력해 주세요")
    num3 = 0
    for j in range(len(List1)):
        num1 = int(input(f"{num2}번째 학생의 {List1[num3]} 점수를 입력해주세요:"))
        List2.append(num1)
        num3 = num3 + 1
    if num2 == 1:
        no1Student.extend(List2)
    elif num2 == 2 :
        no2Student.extend(List2)
    elif num2 == 3 :
        no3Student.extend(List2)
print(no1Student)
print(no2Student)
print(no3Student)

result = Score(no1Student,no2Student,no3Student)

print(f"1번째 학생의 평균 값은 {result[0]} 입니다.")
print(f"2번째 학생의 평균 값은 {result[1]} 입니다.")
print(f"3번째 학생의 평균 값은 {result[2]} 입니다.")