class Person:
  org = "Valve"

  def __init__(self, name):
    self.name = name

  def introduce(self):                    #self is mandatory
    print("Hello, my name is " + self.name + " and I work at " + self.org)

print(Person.org) #accessing class variable without creating an object
p1 = Person("Ben")
p1.introduce() 
print(p1.org) #accessing class variable using object