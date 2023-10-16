print("enter ur phone number")
num=str(input(""))
length=len(num)
while True:
          if length ==10:
                    break
          else:

                  num=str(input("re-enter your phone number :"))
          length=len(num)
lst = []
while num:
    lst.append(num[:2])
    num = num[2:]
print("this is your phone number --------->","+213 (0)",end="")
SIM=str(lst[0]).lstrip('0')
print(SIM,end=" ")
for i in range(1,5):
        print(lst[i],end=" ")

