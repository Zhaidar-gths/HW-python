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