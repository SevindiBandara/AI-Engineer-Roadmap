class cat:
    def sound(self):
        return "Meow"
    
class dog:
    def sound(self):
        return "Woof"
    
animals = [cat(), dog()]

for animal in animals:
    print(animal.sound())  # Calls the sound method of each animal class