class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Patrick", "Jane")
x.printname() 

class Someone(Person):
  pass  #to not add any other properties or methods


class One(Person):
  def __init__(self, fname,lname):
    Person.__init__(self, fname, lname)  #using the parent class constructor

y=One("Patrick", "Jane")
y.printname()
