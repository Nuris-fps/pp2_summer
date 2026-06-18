def awper(*sniper):                         
  print("The top awpers are " + sniper[2])

awper("S1mple", "Zywoo", "Kennys")  #tuple argument. * allows to accept any numbers of positional arguments

def greetings(greeting, *alias):    #mixing *args with regular params
  for name in alias:
    print(greeting,name)
greetings("Hello goat","S1mple","Zywoo","kennys")

def sum(*numbers):        #sum of any amount of values
  total = 0
  for num in numbers:
    total += num
  return total

print(sum(1, 2, 3))
print(sum(10, 20, 30))
print(sum(2)) 

def awper(**standing):                                    #accept any numbers of keywords arguments
  print("The top 1 awper is " + standing["goat"])
  print("The current top awper is " + standing["second"])
  print("The old era goat is" + standing["third"])

awper(goat="S1mple", second = "Zywoo", third = "Kennys")

def awper_info(alias, *args, **kwargs):
  print("Nick:", alias)
  print("realname:", args)
  print("bio:", kwargs)

awper_info("S1mple", "Oleksandr", "Kostylev", age = 28, city = "Kiev") 
awper_info("Kennys", "Kennys", "Shrub", age = 31, city = "Marseille")

def summ(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = summ(*numbers) # Same as: summ(1, 2, 3)
print(result) 

def name(name, surname):
  print("Hello", name, surname)

awper_name = {"name": "Oleksandr", "surname": "Kostylev"}
name(**awper_name) # Same as: name(name="Oleksandr", surname="Kostylev") 