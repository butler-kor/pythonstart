# # 1단계) 2개의 입력을 받는 자동 사칙 연산 계산기
#
# FirstNum = int(input("첫번째 숫자를 입력하세요:"))
# ScondNum = int(input("두번째 숫자를 입력하세요:"))
# print(f"더하기는 {FirstNum + ScondNum}입니다.")
# print(f"빼기는 {FirstNum - ScondNum}입니다.")
# print(f"곱하기는 {FirstNum * ScondNum}입니다.")
# print(f"나누기는 {FirstNum / ScondNum}입니다.")
#
#
# #2단계)2개의 입력과 연산자를 입력받는 계산기
#
# FirstNum = int(input("첫번째 숫자를 입력하세요:"))
# ScondNum = int(input("두번째 숫자를 입력하세요:"))
# Operator = input("연산자를 입력하세요:")
#
# if Operator == "+" or Operator == "더하기":
#     print(f"{FirstNum + ScondNum}")
# elif Operator == "-" or Operator == "빼기":
#     print(f"{FirstNum - ScondNum}")
# elif Operator == "*" or Operator == "곱하기":
#     print(f"{FirstNum * ScondNum}")
# elif Operator == "/" or Operator == "나누기":
#     print(f"{FirstNum / ScondNum}")
# else:
#     print("잘못된 연산자 입니다.")
#
#
#
#
# #3단계) 사용자에게 입력 데이터의 개수를 받아 n개의 데이터에 대한 n개의 연산처리 기능 추가
#
# import operator
# InputNum1 = int(input("데이터 개수를 몇개로 할까요:"))
# Operator = [operator.add, operator.sub, operator.mul, operator.truediv]
# OperatorSymbols = ["+" , "-" , "*" , "/"]
# num1 = 0
# num2 = 0
# num3 = 0
# List1 = []
# while num1 < InputNum1:
#     num2 = int(input(f"{num1+1}번째 데이터를 입력하세요:"))
#     List1.append(num2)
#     num1 = num1 + 1
# num1 = 0
# while num1 < InputNum1 - 1 :
#     Op = Operator[num1]
#     Sym = OperatorSymbols[num1]
#     result = Op(List1[num1], List1[num1 + 1])
#     print(f"{List1[num1]} {Sym} {List1[num1 + 1]} = {result}")
#     num1 = num1 + 1
# print(num3)

#4단계) 사용자에게 종료 여부를 입력 받는 반복 기능 추가

while True:
    FirstNum = int(input("첫번째 숫자를 입력하세요:"))
    Operator = input("연산자를 입력하세요:")
    ScondNum = int(input("두번째 숫자를 입력하세요:"))


    if Operator == "+" or Operator == "더하기":
        print(f"{FirstNum + ScondNum}")
    elif Operator == "-" or Operator == "빼기":
        print(f"{FirstNum - ScondNum}")
    elif Operator == "*" or Operator == "곱하기":
        print(f"{FirstNum * ScondNum}")
    elif Operator == "/" or Operator == "나누기":
        print(f"{FirstNum / ScondNum}")
    else:
        print("잘못된 연산자 입니다.")
    str1 = input("계속하시겠습니까 (Y)(1번) , (N)(2번):")
    if str1 == "N" or str1 == "n" or str1 == "2":
        break
    else:
        print("잘못된 번호 입니다 다시 시작합니다.")
        continue
