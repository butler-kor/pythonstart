import random
List = [1,[1,3,8,],2,3,4,5,6,7,8,9,10]
Choice1 = random.choice(List)
Choice2 = random.choice(List)
print(Choice1)
print(Choice2)
if Choice1 == List[1]:
    Choice1 = random.choice(List[1])
    Choice1 = 'S' + str(Choice1)
print(Choice1)
if Choice2 == List[1]:
    Choice2 = random.choice(List[1])
    Choice2 = 'S' + str(Choice2)
print(Choice2)

while True:
    if 'S' in Choice1 and 'S' in Choice2:
        print(f"{Choice1} {Choice2} 광땡 입니다.")
    elif Choice1 == Choice2:
        print(f"{Choice1} 땡입니다.")
    else:
        print(f"{Choice1 + Choice2}끗입니다.")
    break