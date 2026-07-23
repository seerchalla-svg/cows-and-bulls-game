def norep():
    a1=input('Enter your number')
    ap=list(a1)
    for ka in ap:
         if ap.count(ka) !=1 or len(ap) !=3:
             print('Please Enter a valid number')
             return norep()
    return a1
         
        
import random
Name=input('Enter your name:')
print(f'Hi {Name}, welcome to the MHA game!!')
first = random.choice(range(1, 10))       # 1-9, no zero
rest = random.sample([d for d in range(0, 10) if d != first], 2)  # 2 unique digits, excluding first
a = first*100 + rest[0]*10 + rest[1]
x=a%10
y=int((a/10)%10)
z=int(a/100)  
b1=[z,y,x]
print('you have 8 guesses to guess a 3 digit number, the number does not allow repeation in digits.') 
print('KACCHAN represents the no.of digits that are correct and placed in correct position and DEKU represents the no.of correct digits')
deku=0
kacchan=0
for i in range (1,9):
    a2=norep()
    b2=list(a2)
    for j in range (3):
        if int(b2[j]) == b1[j]:
            kacchan+=1
        elif b1.count(int(b2[j])) == 1:
            deku+=1
    print(f'{a2}     KACCHAN={kacchan}      DEKU={deku}')
    if kacchan ==3:
        break
    if (8-i) != 0:
        print(8-i,'tries left')
    deku=0
    kacchan=0
if kacchan != 3:
    print('The number is ',a)
elif kacchan==3:
    print('YEAHH!! the number is',a)
print(f'Thank you {Name}, for playing MHA')
