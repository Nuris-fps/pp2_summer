def greeting():
    return "Greeeetings"
greeting() # this won't print anything because we are not printing the return value of the function

print(greeting()) # this will print the return value of the function

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

f77=fahrenheit_to_celsius(77)    
print(f77)                          #print required to output return here
print(fahrenheit_to_celsius(50)) 
