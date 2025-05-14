import random
List = [1,[1,3,8,],2,3,4,5,6,7,8,9,10]
<<<<<<< HEAD
Pedigree = ['새륙','장사','장핑','구핑','독사','알리']
Choice1 = random.choice(List)
if Choice1 == List[1]:
    Choice1 = random.choice(List[1])
    Choice1 = 'S' + str(Choice1)
    if Choice1 == 'S1':
        del List[1][0]
    if Choice1 == 'S3':
        del List[1][1]
    else:
        del List[1][0]
print(Choice1)
Choice2 = random.choice(List)
=======
Choice1 = random.choice(List)
Choice2 = random.choice(List)
print(Choice1)
print(Choice2)
if Choice1 == List[1]:
    Choice1 = random.choice(List[1])
    Choice1 = 'S' + str(Choice1)
print(Choice1)
>>>>>>> f9815c3624f4fafe9448a250ffdb07e1e71cf5c6
if Choice2 == List[1]:
    Choice2 = random.choice(List[1])
    Choice2 = 'S' + str(Choice2)
print(Choice2)
<<<<<<< HEAD
#땡이 나오는 조건
if (Choice1 == 'S1' or Choice1 == 'S3' or Choice1 == 'S8') and (Choice2 == 'S1' or Choice2 == 'S3' or Choice2 == 'S8'):
   print(f"{Choice1} {Choice2} 광땡 입니다.")
elif Choice1 == Choice2:
    print(f"{Choice1}땡입니다.")
elif Choice1 == 1 and Choice2[1][0] or Choice2 == 1 and Choice1[1][0]:
    print(f"{Choice1}땡입니다.")
elif Choice1 == 3 and Choice2[1][1] or Choice2 == 3 and Choice1[1][1]:
    print(f"{Choice1}땡입니다.")
elif Choice1 == 8 and Choice2[1][2] or Choice2 == 3 and Choice1[1][2]:
    print(f"{Choice1}땡입니다.")
=======

while True:
    if 'S' in Choice1 and 'S' in Choice2:
        print(f"{Choice1} {Choice2} 광땡 입니다.")
    elif Choice1 == Choice2:
        print(f"{Choice1} 땡입니다.")
    else:
        print(f"{Choice1 + Choice2}끗입니다.")
    break
>>>>>>> f9815c3624f4fafe9448a250ffdb07e1e71cf5c6
