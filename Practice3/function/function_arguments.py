def my_function_with_args(greeting, username):     
    print(f"{greeting}, {username}! using print")           

def my_function_with_args2(greeting, username):     
    return f"{greeting}, {username}! with return"           

print(my_function_with_args("Hellooo","John"))
print("second function with return value:")
print(my_function_with_args2("Hellooo","John"))

def sum(a, b):
    return a+b 
res=sum(6,8)
print(res ) 
print(sum(6,8)) #same as above but without storing the result in a variable first


def aka(name = "zywoo"):
  print("Hello greatest snipers", name)

aka("Kennys")
aka("s1mple")
aka()              #will print zywoo
aka("M0nesy") 
aka(name="S0lek")

def fruit_func(fruits):
  for fruit in fruits:
    print(fruit)

fruit = ["apple", "banana", "cherry"]
fruit_func(fruit) 