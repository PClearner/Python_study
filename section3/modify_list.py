motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('klii')
print(motorcycles)

motorcycles.insert(0,'lover')
print(motorcycles)      # place "0" we insert is the first place in this list
motorcycles.insert(6,'mmkk')
print(motorcycles)      # if the index is bigger than capacity, python will choose the end in this list to append element

del motorcycles[1]
print(motorcycles)

value = motorcycles.pop()
print(motorcycles)
print(value)

value = motorcycles.pop(2)
print(motorcycles)
print(value)

motorcycles.remove('yamaha')
print(motorcycles)      #just only delete once.if you want to clear it completely, you need to use this function more times 

#test
dinner = ['alice','ross','chandeler','monica']
invite_begin = 'we invite friends: '
invite_end =  'to enjoy out dinner'
print(invite_begin,end = '')
for guy in dinner:
    print(guy,end = ' ')
print(invite_end)

dinner[0] = 'jason'
print(invite_begin,end = '')
for guy in dinner:
    print(guy,end = ' ')
print(invite_end)

dinner.append('joey')
dinner.insert(0,'washon')
dinner.insert(round(len(dinner)/2),'jack')
print(invite_begin,end = '')
for guy in dinner:
    print(guy,end = ' ')
print(invite_end)

print("I just can invite two guest because of the table I have bought wasn't brought in time")
size = len(dinner)
while size != 2:
    print(f"Dear {dinner.pop().title()}, I am so sorry that i can't invite you to enjoy my dinner")
    size = size -1
print(invite_begin,end = '')
for guy in dinner:
    print(guy,end = ' ')
print(invite_end)
del dinner[0]
del dinner[0]
print(dinner)