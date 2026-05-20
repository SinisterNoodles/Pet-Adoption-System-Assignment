# Name:
# Date:
# Program: Mini Pet Adoption System

animals = {}

class Pet:
    def __init__(self, name, age, animalType, breed):
        self.name = name
        self.age = age
        self.animalType = animalType
        self.breed = breed

    def showInfo(self):
        print(f"Pet name: {self.name.title()}\n"
              f"Pet age: {self.age}\n"
              f"Pet animal type: {self.animalType.title()}\n"
              f"Pet breed: {self.breed.title()}")

class Dog(Pet):
    def __init__(self, name, age, animalType, breed, bark):
        super().__init__(name, age, animalType, breed)
        self.bark = bark

    def showInfo(self):
        super().showInfo()
        print(f"Bark type: {self.bark.title()}")

"""class Cat(Pet):
    def __init__(self, name, age, animalType, breed, bark):
        super().__init__(name, age, animalType, breed)

    def showInfo(self):
        super().showInfo()"""

def basicTraits(animal):
    name = input(f"Enter {animal}'s name: ").lower().strip()
    breed = input(f"Enter {animal}'s breed: ").lower().strip()
    while True:
        try:
            age = int(input(f"Enter {animal}'s age: "))
            break
        except ValueError:
            print("Please enter a valid age")
    return name, age, breed

def listAnimals():
    for animal in animals:
        print(animal.title())

def findAnimal():
    return input("Select your animal (name): ").lower().strip()

def showInfo():
    animal = animals.get(findAnimal())
    if animal:
        animal.showInfo()
    else:
        print("Animal does not exist")

def destroyAnimal():
    animal = findAnimal()
    if animal in animals:
        del animals[animal]
    else:
        print("Animal does not exist")

def createDog():
    name, age, breed = basicTraits("dog")
    bark = input("Enter dog's bark type: ")
    animals[name] = Dog(name, age, "dog", breed, bark)

while True:
    match input("1. Create animal | 2. List Animals | 3. Show info | 4. Destroy animal | 5. Exit: ").strip():
        case "1":
            createDog()
        case "2":
            listAnimals()
        case "3":
            showInfo()
        case "4":
            destroyAnimal()
        case "5":
            break
        case _:
            print("Invalid input")