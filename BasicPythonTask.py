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
<<<<<<< HEAD
# InputNum = int(input("정수를 입력하세요:"))
# num1 = 1
# num2 = 1
# while num1 <= InputNum:
#     num2 *= num1
#     num1 += 1
# print(num2)

# 약수구하기
FirstNum = int(input("첫번째 숫자를 정수로 입력하세요:"))
SecondNum = int(input("두번째 숫자를 정수로 입력하세요:"))
List1 = []
List2 = []
num1 = 0
num2 = 0
num3 = 0
num4 = 0
for i in range(1,FirstNum + 1):
    if FirstNum % i == 0:
        List1.append(i)
for j in range(1,SecondNum + 1):
    if SecondNum % j == 0:
        List2.append(j)
print(List1)
print(List2)
