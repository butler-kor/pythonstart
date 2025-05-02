month = (31,28,31,30,31,30,31,31,30,31,30,31)
day = ("월요일","화요일","수요일","목요일","금요일","토요일","일요일")
HollyDay = {"01월 01일":["구정"], "12월 25일":["크리스마스"]}
InputMonth = int(input("월을 입력하세요:"))
InputDay = int(input("일을 입력하세요:"))
num1 = 0
num2 = 0
while num1 < InputMonth-1:
    num2 += month[num1]
    num1 = num1 +1
num2 = num2 + InputDay
num1 = (num2 % 7) + 1
print(num2)
print(day[num1])
Quist = int(input("공휴일을 찾아 보시겠습니까? Y(1번) , N(2번)"))
InputHollyDay = input("공휴일명을 입력하세요 (예) 구정 , 신정 , 크리스마스 등 ")
if InputHollyDay :
    if InputHollyDay in HollyDay:
        OutputHollyDay = HollyDay.get(InputHollyDay)
        print(f"선택하신 {InputHollyDay}는 {}")