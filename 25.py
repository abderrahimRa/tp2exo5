print("u should enter X , Y , Z , T  so it can be in format XYhZT"  )
num=input("enter")
while True:
    if (len(num)==5):
        break
    else:
        num=input(" re enter the value please on the next format : XYHZT ---->  ")
lst = []
while num:
    lst.append(num[:1])
    num = num[1:]
lst.remove('h')    
for i in range(len(lst)):
    lst[i]=int(lst[i])
heur= lst[0]*10+lst[1]
minute= lst[2]*10+lst[3]
if heur<0 or heur>24 or minute<0 or minute>60:
    print("horaire est faux :) ")
else:
    for i in range(len(lst)) :
        print(lst[i],end="")
        if i==1:
            print("h",end="")
