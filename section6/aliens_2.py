pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']}")

for t in pizza['toppings']:
    print(t,end = ' ')
print()

#test
a = {'name':'stiff','city':'New York','age':'18'}
b = {'name':'xx','city':'Shanghai','age':'18'}
c = {'name':'looc','city':'Paris','age':'18'}
people = [a,b,c]
for i in people:
    print(i)


a1 = {'animal':'cat','owner':'jack'}
a2 = {'animal':'dog','owner':'sack'}
a3 = {'animal':'bird','owner':'shack'}
pets = [a1,a2,a3]
for p in pets:
    print(p)



favorite_places = {
    'hack':['china','usa','tailand'],
    'chaer':['usa','shanghai'],
    'llsk':['cascvv','kojnooav'],
}
for k,v in favorite_places.items():
    print(f"{k} love play in these place:",end = ' ')
    for x in v:
        print(x,end = ' ')
    print()


cities = {
    'shanghai':{'country':'china','population':1235,'fact':'Unknown'},
    'guangzhou':{'country':'china','population':27381,'fact':'Unknown'},
    'beijing':{'country':'china','population':98658,'fact':'Unknown'}
}
for k,v in cities.items():
    print(f"{k}:",end = '\n\t')
    for k1,v1 in v.items():
        print(f"{k1}:{v1}",end = '\n\t')
    print()

