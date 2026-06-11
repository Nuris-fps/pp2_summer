print(bool("Hello")) #returns True
print(bool(15)) #returns True

print(bool(False)) #returns False
print(bool("")) #returns False
print(bool(0)) #returns False
print(bool([])) #returns False. goes same for {} and ()

#print is not necessary here

def myFunction() :
  return True

print(myFunction()) #prints True

x = 200
print(isinstance(x, int)) #prints True because x is an integer