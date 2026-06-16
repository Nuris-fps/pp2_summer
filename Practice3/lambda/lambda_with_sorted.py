stud = [("Emil", 25), ("Tobias", 22), ("Linus", 21)]
sorted_stud = sorted(stud, key=lambda x: x[1]) #sorted use lambda to sort by age (x[1]) instead of name (x[0])
print(sorted_stud)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))  #sort by length 
reverse_words = sorted(words, key=lambda x: len(x), reverse=True) #reverse the order of sorted list
print(sorted_words)
print(reverse_words)