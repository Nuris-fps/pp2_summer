import json

# JSON:
x =  '{ "name":"Ben", "age":35, "city":"London"}'

#json to python conversion
y = json.loads(x)         # parse x. convert to a dictionary

print(y)                  # the result is a Python dictionary 
print(y["city"])          # output: London


d={
    "name": "Bernard",
    "age": 20,
    "city": "Manchester"
}

# python to json conversion
t = json.dumps(d)             # convert into JSON string    

print(t)                      # the result is a JSON string

# print(t["city"])            # error, because t is a string, not a dictionary
print(json.loads(t)["city"])  # output: Manchester, convert t back to dictionary first

print(json.dumps(("mango", "papaya")))  # output: ["mango", "papaya"]

print(json.dumps(d, indent=4))  # output: JSON string with indentation for better readability
print("separators changed: \":\" to \" = \" and \", \" to \". \" \n" + json.dumps(d, indent=4, separators=(". ", " = ")))  # output: JSON string with custom separators # instead of ":" and "," , it uses " = " and ".  " respectively                                                         
print("sorted keys: \n" + json.dumps(d, indent=4, sort_keys=True))  # output: JSON string with sorted keys