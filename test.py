

class Dog: 
    # Class Attribute
    species = 'mammal'

    #Initialize / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance Method
    def description(self):
        return f"{self.name} is {self.age} years old."

    #Instance Method
    def bark_at(self, other_dog):
        print(f"{self.name} barked furiously at {other_dog.name}")

# nelson = Dog('Nelson', 3)
# print(f"{nelson.name} is {nelson.age}.")

nelson = Dog('Neslon', 3)
baxter = Dog('Baxter', 16)

nelson.bark_at(baxter)

