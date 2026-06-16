class Supernatural(Person):
  def __init__(self, fname, lname, power,universe):
    super().__init__(fname, lname)           #inherit method and properties from the parent class
    self.power = power
    self.universe = universe                 #add properties to the child class

  def printpower(self):
    print(self.firstname, self.lastname, "has the power of", self.power, "in", self.universe)

y = Supernatural("Patrick", "Jane", "pseudo reading of actions and intentions","The Mentalist Universe")
y.printpower()