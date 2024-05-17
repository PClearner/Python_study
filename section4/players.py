players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:-3])

print(players[0:5:2])

for player in players[:3]:
    print(player)
print("next sort")
for player in players:
    print(player)


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(f'this is my food: {my_foods}')
print(f"this is my friend's food: {friend_foods}\n")

my_foods.append('coffee')
friend_foods.append('beef')
print(f'this is my food: {my_foods}')
print(f"this is my friend's food: {friend_foods}\n")


friend_foods = my_foods
print(f'this is my food: {my_foods}')
print(f"this is my friend's food: {friend_foods}\n")
my_foods.append('milk')
friend_foods.append('juice')
print(f'this is my food: {my_foods}')
print(f"this is my friend's food: {friend_foods}\n")
# tip: this copy like the thing in C++ call &.Because if you change 'my_foods' or 'friend_foods',it will change another one.they are not individual

#test:

items = list(range(1,10))
print('The first three items in the list are:',end = ' ')
print(items[:3])
print('Three items from the middle of the list are:',end = ' ')
print(items[3:6])
print('The last three items in the list are:',end = ' ')
print(items[-3:],end = '\n')


my_pizzas = list(range(1,10))
friend_pizzas = my_pizzas[:]
friend_pizzas.append(100)
print('My favorite pizzas are:',end = ' ')
for f in my_pizzas:
    print(f,end = ' ')
print(f"\nmy friend's favorite pizzas are:",end = ' ')
for f in friend_pizzas:
    print(f,end = ' ')

#practice 4.12: it is so boring!!!