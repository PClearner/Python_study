cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
        print(car.lower())
    else:
        print(car.title())


ss = 'llkknn'
if ss != 'n n':
    print(ss)

an = 18
if an != 19:
    print(an)

value = 99
if value <=90:
    print(value)
else:
    print(90)

value = [10,12]
if value[0]>5 and value[1]< 15:
    print("value ok in and test")

if value[0]>20 or value[1] <20:
    print("value ok in or test")

ccas = ['asddas','casczx','acqwgaf','sahqdfsg']
if 'asddas' in ccas:
    print("asddas is in ccas")
if 'gg' not in ccas:
    print("gg is not in ccas")

#test:
#this practice is so boring,because I have learned C++ so that I am familiar with "if" .add()


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $50.")


if age < 4:
    price = 0
elif age<18:
    price = 25
else:
    price = 50

print(f"Your admission cost is ${price}.")

#test:
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print('green is in alien_color')
    if 'black' not in alien_color:
        print('black is not in alien_color')
    elif 'orange' not in alien_color:
        print("orange is not in alien_color")
elif 'yellow' in alien_color:
    print('yellow is in alien_color')


age =77
if age <2:
    print('he is a infant')
elif age > 2 and age <4:
    print('he is a baby')
elif age>4 and age <13:
    print("he is a children")
elif age >13:
    print("he is a teenager")


