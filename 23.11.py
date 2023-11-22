#task1

age=int(input('enter your age: '))
if age<0:
    print('age should be grater than zero')
else:
    if age >= 18:
        print('you are old enogh to learn to drive ')
    else:
        print(f'your need {18 - age } more years to learn to drive')

#task2
age=int(input('enter your age: '))

if age>0 and age>=18:
    print("your are old enogh to learn to drive  ")
elif age > 0 and age < 18: 
    print(f'your need {18 - age } more years to learn to drive')
else:
    print('age should be grater than zero')



# task3
a=int(input("number one") )
b=int(input('number two'))
if a==b :
 print("Сандар тең")
elif a>b :
    print("Бірінші сан үлкен")
else:
 print("Екінші сан үлкен")

 #livel 2

 #task 1
 #x= int(input("Балыңызды енгізіңіз: ")) 
#if x >= 90 and x <= 100:
 #  print ("A")
#elif  x>=80 and x<90 :
 #  print("B")
#elif  x>=70 and x<80 :
#   print("C")
#elif  x>=60 and x<70:
 #  print("D")
#elif  x>=0 and x<60 :
 #  print("F")
#else:
#	print("Error")


#task2

# month=input("Enter a month : ")
# if month=="June" or month=="July" or month=="August":
#     print("Sammer")
# elif month=="September" or month=="October" or month== "November ":
#     print("Autumn")
# elif month=="Desember" or month== "February" or month=="January":
#     print("Winter")
# else :
#   print("Spring")