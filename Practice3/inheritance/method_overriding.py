class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    # This overrides the parent's speak method
    def speak(self):
        return "Woof!"

# Usage
generic_animal = Animal()
rex = Dog()

print(generic_animal.speak())  # Output: Generic animal sound
print(rex.speak())             # Output: Woof!
