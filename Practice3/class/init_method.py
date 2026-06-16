class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ben", 25)

print(p1.name)
print(p1.age) 

class Person_def_value: 
  def __init__(self, name,surname, age=18):        #set default value for age
    self.name = name
    self.surname = surname
    self.age = age

p1 = Person("Ben", "Ten")
p2 = Person("Dan", "Madisclaire", 34)

print(p1.name, p1.surname, p1.age)
print(p2.name, p2.surname, p2.age) 