requested_toppings = ['mushroom','green peppers','extracheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"sorry, we are out of {requested_topping} right now")
    else:
        print(f"Adding {requested_topping}.")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?\n")

#test:
user = ['admin','hack','jack','amy','star']
if user:
    for u in user:
        if u.title() == 'Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {u}, thank you for logging in again')
else:
    print("We need to find some users")


current_users = ['admin','hack','jack','lihua','jason','chandeler','monica']
new_users = ['admin','hack','jack','amy','star']
for u in new_users:
    if u in current_users or u.title() in current_users or u.upper() in current_users:
        print(f'this name {u} is used,please change another')
    else:
        print(f'this name {u} is not used,completely create a new name')
    
#practice 5.11:it is so boring(haha,I forget that how much times I say this sentence)


