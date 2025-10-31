# 55. Inheritance example with animal → dog.
# Parent Class
class DomesticAnimal:
    def __init__(self, size, mood):
        self.size = size
        self.mood = mood

    def description(self):
        print(f"Size: {self.size}, Mood: {self.mood}")

    def speak(self):
        print("This animal makes a sound.")

# Child Class - Dog
class Dog(DomesticAnimal):
    def speak(self):
        print("Woof! 🐶 I am a friendly dog.")

# Child Class - Cat
class Cat(DomesticAnimal):
    def speak(self):
        print("Meow! 🐱 I like my own space.")

# Function to determine and create the animal
def user():
    size = int(input("Enter size of animal (int): "))
    mood = input("Enter mood of animal (friendly / alonelover): ").lower()

    if size >= 16 and mood == "friendly":
        animal = Dog(size, mood)
    elif size < 16 and mood == "alonelover":
        animal = Cat(size, mood)
    else:
        print("The animal does not exist in our database. Try another.")
        return

    # Show details
    animal.description()
    animal.speak()

# Run program
user()

