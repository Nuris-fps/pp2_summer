class MyClass:
  x = "Hello worker"
  y= "Felps"


p1 = MyClass() #create an object p1 of class MyClass
print(p1.x,p1.y) 

del p1 #delete the object p1

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)  #create 3 objects from same class

class Person:
  pass #pass is to create an empty class. without pass, we would get an error