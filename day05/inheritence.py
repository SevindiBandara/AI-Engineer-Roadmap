# parent class 
class Animal: 
    
    def eat(self):
        return "I can eat"
    
# child class
class Dog(Animal):
    def bark(self):
        return "woof woof"
    
dog = Dog()
print(dog.eat())  # Inherited method from Animal class
print(dog.bark())  # Method from Dog class

