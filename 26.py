number=int(input("enter the number : "))
num=str(number)
while True:
       if number<0 or  number>999:
          number=int(input("enter the number : "))
          num=str(number)
       else:
             
             break
       
frdi=["","un","deux","trois","quatre","cinq","six","sept","huit","neuf"]
ochri=["","dix","vignt","trente","quarante","ciquante","soixante","soixante dix","quatrevingts","quatrevingts-dix"]
tentotweny=["dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf"]
lst=[]
while num:
       lst.append(num[:1])
       num = num[1:]
for i in range(len(lst)):
    lst[i]=int(lst[i])

if number>=200:
       if (number-lst[0]*100)>69 and((number-lst[0]*100)<=79):
          print(frdi[lst[0]],"cent",ochri[6],tentotweny[lst[2]])
       else:
          print(frdi[lst[0]],"cent",ochri[lst[1]],frdi[lst[2]])
elif number>=100 and number<200:
       if (number-lst[0]*100)>69 and((number-lst[0]*100)<=79):
          print("cent",ochri[6],tentotweny[lst[2]])
          
       else:
            print("cent",ochri[lst[1]],frdi[lst[2]])
elif number<100 and number>=20 :
       print(ochri[lst[0]],frdi[lst[1]])
elif number>10 and number<20 :
      print(tentotweny[lst[1]-1])
elif number<10 and number>0:
       print(frdi[number])
else:
     print("zero :) ")
