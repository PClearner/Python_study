user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last': 'fermi'
}

for k,v in user_0.items():
    print(f"key is {k},value is {v}")

for k in user_0.keys():
    print(f"key is {k}")

for k in user_0:
    print(f"k is {k}")
    
for k in sorted(user_0.keys()):
    print(k,end=' ')
print()

for k in user_0.values():
    print(k,end = " ")
print()

for k in set(user_0.values()):
    print(k,end = " ")

#test

river = {
    'Yangtze River':'China',
    'Nilo River': 'Tailand',
    'ssc River': 'Unknown'
}
for k,v in river.items():
    print(f"The {k} runs through {v}")
for k in river:
    print(k,end = ' ')
print()
for v in river.values():
    print(v,end = ' ')


