# test
answer = ""
while answer != "quit":
    answer = input("what you need: ")
    if answer != "quit":
        print(f"you need {answer}")


answer = ""
while answer != "quit":
    answer = input("the age of the audience: ")
    if answer != "quit":
        if int(answer) < 3:
            print("the audience get a free ticket")
        elif int(answer) >= 3 and int(answer) < 12:
            print("the audience need to pay 10 dollor")
        else:
            print("the audience need to pay 15 dollor")
