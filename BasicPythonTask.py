#  1부터 100까지 더하기
#  while 문을 사용하여 더하기
# num1 = 0
# num2 = 0
# while num1 <= 100:
#     num2 += num1
#     num1 = num1 + 1
# print(num2)
#
# for 문을 사용하여 더하기
# num3 = 0
# for i in range(101):
#     num3 += i
# print(num3)
#
#
# 1부터 100까지 숫자 중에서 짝수만 더하기
# num1 = 0
# num2 = 0
# while num1 <=100 :
#     if num1 % 2 == 0:
#         num2 += num1
#     num1 = num1 + 1
# print(num2)
#
# num1 = 0
# for i in range(101):
#     if i % 2 == 0:
#         num1 += i
# print(num1)
#
#  리스트를 만들고 숫자를 하나 받은 후 리스트 안에서 받은 숫자보다 작은 숫자만 출력
# List1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# List2 = []
# Innum1 = int(input("숫자를 정수로 입력하세요:"))
# num1 = 0
# num2 = 0
# while num1 < len(List1):
#     if List1[num1] < Innum1 :
#         num2 = List1[num1]
#         List2.append(num2)
#     num1 = num1 + 1
# print(List2)
#
# 리스트를 랜덤으로 만들고 숫자를 하나 받은 후 리스트 안에서 받은 숫자보다 크면 출력
# import random
# List3 = []
# InputNum1 = int(input("랜덤 숫자를 몇개를 만들까요?"))
# InputNum2 = int(input("비교할 숫자를 정수로 입력하세요"))
# num1 = 0
# num2 = 0
# while num1 < InputNum1:
#     num2 = random.randint(1,100)
#     if num2 > InputNum2:
#         List3.append(num2)
#     num1 = num1 + 1
# print(List3)
from autopep8 import continued_indentation

#  글자로 숫자를 입력 받은 후 그 글자형 숫자를 정수로 변환하여 더하고 출력
# InputStr = input("숫자를 정수로 2자리 이상 입력하세요 : ")
# num1 = 0
# num2 = 0
# while num1 < len(InputStr):
#     num2 += int(InputStr[num1])
#     num1 += 1
# print(num2)

# 1부터 어떤 양의 정수n까지의 정수를 모두 곱한 값을 출력
# Inputnum = int(input("정수 N의 값을 정해주세요 : "))
# num1 = 1
# for i in range(1,Inputnum + 1):
#     num1 *= i
# print(num1)

# 거듭제곱 값을 구하기 밑수와 지수의 값을 입력 받은 후 거듭제곱으로 값을 출력
# BaseNum = int(input("밑수를 입력하세요:"))
# ExponentNum = int(input("지수를 입력하세요:"))
# num1 = 0
# num2 = 1
# while num1 < ExponentNum:
#     num2 *= BaseNum
#     num1 = num1 +1
# print(num2)

# 1부터 어떤 양의 정수 N까지의 정수를 모두 곱한 것

# InputNum = int(input("정수를 입력하세요:"))
# num1 = 1
# num2 = 1
# while num1 <= InputNum:
#     num2 *= num1
#     num1 += 1
# print(num2)

# 약수구하기
# FirstNum = int(input("첫번째 숫자를 정수로 입력하세요:"))
# SecondNum = int(input("두번째 숫자를 정수로 입력하세요:"))
# List1 = []
# List2 = []
# num1 = 0
# num2 = 0
# num3 = 0
# num4 = 0
# for i in range(1,FirstNum + 1):
#     if FirstNum % i == 0:
#         List1.append(i)
# for j in range(1,SecondNum + 1):
#     if SecondNum % j == 0:
#         List2.append(j)
# print(List1)
# print(List2)

#등차수열
# List1 = []
# InputNum1 = int(input("등차수열 값을 입력하세요"))
# InputNum2 = int(input("몇개의 수열을 만들까요?:"))
# num1 = 1
# for i in range(1,InputNum2 + 1):
#     List1.append(num1)
#     num1 += InputNum1
# print(List1)

#등비수열
# List1 = []
# InputNum1 = int(input("등비수열 값을 입력하세요"))
# InputNum2 = int(input("몇개의 수열을 만들까요?:"))
# num1 = 1
# for i in range(1,InputNum2 + 1):
#     List1.append(num1)
#     num1 *= InputNum1
# print(List1)
#
# 피보나치수열
# List1 = [1,1]
# num1 = 0
# num2 = int(input("몇개의 수열을 만들까요?:"))
# num3 = 0
# while num1 < num2 - 1:
#     num3 = List1[num1] + List1[num1 + 1]
#     List1.append(num3)
#     num1 += 1
# print(List1)

# #항목 뒤집기
# List1 = ['오징어','문어','돼지고기','소고기','염소고기','닭고기','오리고기']
# List2 = []
# num1 = 0
# num2 = -1
# while num1 < len(List1):
#     List2.append(List1[num2])
#     num1 += 1
#     num2 -= 1
# print(List2)
#
# #리스트 삭제
# List1 = {'오징어': 10000,'문어':15000,'돼지고기':18000,'소고기':25000,'염소고기':19000,'닭고기':18000,'오리고기':17000}
# List2 = ['오징어','문어','돼지고기','소고기','염소고기','닭고기','오리고기']
# print(f"현재 우리가게에 있는 목록은 {List2}입니다.")
# Str1 = input("삭제하고 싶은 리스트를 정해 주세요:")
# while True:
#     if Str1 in List1 and Str1 in List2:
#         del List1[Str1]
#         List2.remove(Str1)
#         print(f"리스트에서 {Str1}를 삭제하였습니다.")
#         print(f"현재 남아있는 리스트는 {List1}입니다.")
#         break

#리스트 삽입
# import random
# List1 = []
# num1 = int(input("몇개의 난수를 만들 것인가요:"))
# num2 = int(input("리스트의 몇번째에 넣을 것인가요?:"))
# num3 = int(input(f"{num2}번째 들어갈 숫자는 무엇인가요:"))
# num4 = 0
# num5 = 0
# while num4 < num2 -1 :
#     num5 = random.randint(1,50)
#     if num5 not in List1:
#         List1.append(num5)
#         num4 = num4 + 1
# List1.append(num3)
# while num4 < num1:
#     num5 = random.randint(1, 50)
#     if num5 not in List1:
#         List1.append(num5)
#         num4 = num4 + 1
# print(List1)

# 250520 중복제외 랜덤숫자 만들기와 리스트 만들기
# import random
# List1 = []
# num1 = int(input("몇개의 랜덤한 숫자를 만들 것인가요?"))
# num2 = int(input("랜덤한 숫자의 범위를 정수로 정해주세요 예) 30 (단 랜던함 숫자보다 작아서는  안됩니다. "))
# num3 = 0
# num4 = 0
# for i in range(1,num1):
#     RandomNum = random.randint(1,num2 + 1)
#     if RandomNum not in List1:
#         List1.append(RandomNum)
# print(List1)
#
# List1 = []
# while num3 < num1:
#     num4 = random.randint(1, num2 + 1)
#     if num4 not in List1:
#         List1.append(num4)
#     num3 = num3 + 1
# print(List1)

# 250520 최대공약수 임의의 숫자 2개를 받아서 2개의 숫자에 최대 공약수를 구하기
# FirstNum = int(input("첫번째 숫자를 입력하세요:"))
# SecondNum = int(input("두번째 숫자를 입력하세요:"))
# num1 = FirstNum
# num2 = 1
# num3 = 1
# if SecondNum < FirstNum:
#     num1 = SecondNum
#
# while num2 <= num1 :
#     if FirstNum % num2 == 0 and SecondNum % num2 == 0:
#         num3 = num2
#     num2 = num2 + 1
# print(num3)

# 250520 2진수 표현 10진수 숫자를 받아서 2진수로 표현하기
# Str1 = ''
# num1 = int(input("이진수로 바뀔 10진수 정수를 입력하세요:"))
# num2 = 1
# num3 = 0
# if num1 == 0 :
#     Str1 = '0'
# # 250521 이어서 작성 수정  나눌 때 1씩 더하는 것이 아니라 나머지가 1이면 1이 0이면 0이 추가되는 방식
# else:
#     while num1 > 0:
#         num2 = num1 % 2
#         Str1 = str(num2) + Str1
#         num1 = num1 // 2
# print(Str1)

# 250521  10진수 표현  2 진수를 받아서 10진수로 표현하기
Str1 = input("2진수 숫자를 입력하세요(2진수는 0과 1로만 이루어진 숫자입니다.):")
Str2 = ''
num1 = 0
num2 = -1
while num1 < len(Str1):
    Str2 = Str2 + Str1[num2]
    num1 = num1 + 1
    num2 = num2 - 1
print(Str2)  # 20250522 추가 작성
num1 = 0
num2 = 0
for i in Str1:
    num1 += int(i) * (2 ** num2)
    num2 = num2 + 1
print(f"2진수 {Str1}을 10진수로 변환하면 {num1}가 됩니다.")