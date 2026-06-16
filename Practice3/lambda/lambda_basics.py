x = lambda a, b : a + b + 10   #any numbers of arguments and single expression
print(x(5,6)) 

def scaler(n):
  return lambda a : a * n 

twicer = scaler(2)         #twicer uses function scaler to scale value of twicer
thricer =scaler(3)

print(twicer(11))          #11*2 = 22
print(thricer(11))         #11*3 = 33
