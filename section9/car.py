#test
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"this restaurant's name is {self.restaurant_name},its cuisine_type is {self.cuisine_type},the number_served is {self.number_served}."
        )

    def open_restaurant(self):
        print("this restaurant is working!!")
        
    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self,n):
        self.number_served += n

r = restaurant("luck","w")
r.describe_restaurant()
r.set_number_served(12)
r.describe_restaurant()
r.increment_number_served(23)
r.describe_restaurant()


class User:
    def __init__(self, first, last, gender, age):
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.age = age
        self.login_attempts = 1

    def describe_user(self):
        print(f"this person's informations:")
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"gender: {self.gender}")
        print(f"age: {self.age}")

    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name},nice to meet you!!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def print_login_attempts(self):
        print(f"login_attempts: {self.login_attempts}")

k = User("xxl","ss","male",19)
k.print_login_attempts()
for i in range(1,4):
    k.increment_login_attempts()
k.print_login_attempts()
k.reset_login_attempts()
k.print_login_attempts()
        


        
