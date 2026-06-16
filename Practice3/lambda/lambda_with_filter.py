numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  #filter creates list of items that return true for function 
print(odd_numbers)                                         #(filter(lambda x: x % 2 != 0, numbers) )
