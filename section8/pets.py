def describe_pet(animal_type,pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
describe_pet(pet_name="harry",animal_type="dog")

def describe_pex(animal_type,pet_name="god"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
describe_pex("cat")
describe_pex("cat","harry")

#test
def make_shirt(size,words = "I love python!"):
    print(f'thsi shirt size is {size}.It need to print words "{words}"')
make_shirt(18,"hop")
make_shirt(size=18,words="hop")

make_shirt('Max')
make_shirt('middle')
make_shirt('middle','hi star!')
