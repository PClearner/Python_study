class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def shear(self):
        print(f"{self.name} shear")


# test
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"this restaurant's name is {self.restaurant_name},its cuisine_type is {self.cuisine_type}."
        )

    def open_restaurant(self):
        print("this restaurant is working!!")


r = restaurant("lucker", "w")
r.describe_restaurant()
r.open_restaurant()


class User:
    def __init__(self, first, last, gender, age):
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"this person's informations:")
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"gender: {self.gender}")
        print(f"age: {self.age}")

    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name},nice to meet you!!")


a = User("jj", "xx", "male", 12)
b = User("xkl", "poller", "female", 18)
a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()
