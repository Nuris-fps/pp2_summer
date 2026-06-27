f = open("demofile.txt")              # default values are "rt". r-read.t-text. b - binary

f = open("demofile.txt","rt")         # same as above

x = open("C:\\Games\sometxt.txt")     #specify file path to open files in different directory
print(x.read())

print(f.read())
f.close() 
"""
You should always close your files. Or use next statement
In some cases, due to buffering, changes made to a file may not show until you close the file.
Or use next statement
"""
with open("demofile.txt") as f:         # with closes file automatically itself. if without it, to close use f.close() 
    print( f.read()) 

with open("demofile.txt") as f:
    print(f.read(5))                    # Return first 5 characters
  
with open("demofile.txt") as f:
  print(f.readline())                   # Return first line

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())                    # Return first 2 lines


with open("demofile.txt") as f:
  for x in f:
    print(x)                             # Read line by line. There will be newline character after each line 