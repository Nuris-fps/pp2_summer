goats = ("zywoo", "s1mple", "dev1ce")
myit = iter(goats)

print(next(myit))
print(next(myit))
print(next(myit))

GOAT = "S1mple"
myit = iter(GOAT)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit)) stop iteration error, because there are only 6 characters in the string "S1mple"

mytuple = ("apple", "banana", "cherry")

for x in mytuple:          #default for loop
  print(x) 

class numbers:
  def __iter__(self):
    self.a = 1
    return self 

  def __next__(self):
    x = self.a
    self.a += 1
    return x     
   
myclass = numbers()
myiter = iter(numbers())  # or iter(myclass)

print(next(myiter))
print(next(myiter)) 
print(next(myiter))

class StoppedNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = StoppedNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)