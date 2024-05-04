for value in range(1,5):        # it only print 1~4
    print(value,end = ' ')

print("\n")

for value in range(6):
    print(value,end = ' ')

print("\n")
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

print("\n")
digits = list(range(1,10))
digits.append(0)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

print("")
squares = [ value ** 2 for value in range(1,11)]
print(squares)
squares = [value ** 2 for value in squares]
print(squares)

#test
for v in range(1,21):
    print(v,end = ' ')
print('')

#practice4.4: it waste my time so that i give up to do it

testlist = list(range(1,1_000_001))
print(sum(testlist))
print(max(testlist))
print(min(testlist))

print('')
for value in range(1,21,2):
    print(value,end = ' ')
print('')

for value in range(3,31):
    if value%3 == 0:
        print(value,end = ' ')
print('')

for value in range(1,11):
    print(value**2,end=' ')
print('')

creat_numbers = list(value**2 for value in range(1,11))
print(creat_numbers)
