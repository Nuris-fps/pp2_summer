import datetime

x = datetime.datetime.now()  
print(x) 

print(x.year)             # 2026 
print(x.strftime("%y"))   # 26 , Y for 2026
print(x.strftime("%A"))   # Thursday  
print(x.strftime("%a"))
print(x.strftime("%B"))   # June
print(x.strftime("%b"))   # Jun

print("Weekday number is: " + x.strftime("%w")) 

print("Hour of time is: " +x.strftime(%H) )   # 14 or 02 if %l
print(x.strftime("%p"))   # AM or PM

print(x.strftime("%M"))   # 51 


dr = datetime.datetime(2007,1,31)   # 2007-01-31 00:00:00
print(dr)

