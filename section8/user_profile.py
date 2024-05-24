# test
def sandwichs(*food):
    print("this sandwich need the foods:", end=" ")
    for x in food:
        print(x, end=" ")
    print()


sandwichs("apple", "banana", "jam", "orange")


def user_profile(first, last, **user):
    user["first_name"] = first
    user["last_name"] = last
    return user


uu = user_profile("zhang", "yao xing", country="china", city="guangzhou")
print(uu)


def make_car(maker, type, **informations):
    informations["company"] = maker
    informations["type"] = type
    return informations


mm = make_car("subaru", "outback", color="blue", tow_packing=True)
print(mm)
