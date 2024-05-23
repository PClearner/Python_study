# test

car = input("tell me what car you want to rent: ")
print(f"let me see if I can find you a {car}")

people = input("please tell me how many persons will come to have a meal: ")
people = int(people)
if people > 8:
    print("there is no table for more than eight persons")
else:
    print("there is a table for you")

value = input("please input a number: ")
if int(value) % 10 == 0:
    print("True")
else:
    print("False")
 