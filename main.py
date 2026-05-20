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

class Cat(Pet):
    def __init__(self, name, age, animalType, breed, furColour):
        super().__init__(name, age, animalType, breed)
        self.furColour = furColour

    def showInfo(self):
        super().showInfo()
        print(f"Fur colour: {self.furColour}")

def getInput(animal, parameter):
    while True:
        parameterInput = input(f"Enter {animal}'s {parameter}: ").lower().strip()
        if parameterInput:
            return parameterInput
        else:
            print(f"Invalid {parameter} input")

def checkValid(function):
    if animals:
        function()
    else:
        print("There are no current animals")

def basicTraits(animal):
    name = getInput(animal, "name")
    breed = getInput(animal, "breed")
    while True:
        try:
            age = int(input(f"Enter {animal}'s age: "))
            break
        except ValueError:
            print("Please enter a valid age")
    return name, breed, age

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

def giveUpAnimal():
    animal = findAnimal()
    if animal in animals:
        del animals[animal]
        print(f"{animal.title()} has been given away")
    else:
        print("Animal does not exist")

def adoptDog():
    animalType = "dog"
    name, breed, age = basicTraits(animalType)
    bark = getInput(animalType, "bark type")
    animals[name] = Dog(name, age, animalType, breed, bark)

def adoptCat():
    animalType = "cat"
    name, breed, age = basicTraits(animalType)
    furColour = getInput(animalType, "fur colour")
    animals[name] = Cat(name, age, animalType, breed, furColour)

while True:
    match input("1. Adopt animal | 2. List Animals | 3. Show info | 4. Give up animal | 5. Exit: ").strip():
        case "1":
            match input("Enter species of animal: ").lower().strip():
                case "dog":
                    adoptDog()
                case "cat":
                    adoptCat()
                case _:
                    print("Unavailable species")
        case "2":
            checkValid(listAnimals)
        case "3":
            checkValid(showInfo)
        case "4":
            checkValid(giveUpAnimal)
        case "5":
            break
        case _:
            print("Invalid input")