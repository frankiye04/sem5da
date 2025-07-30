# ex2.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squares = [x ** 2 for x in numbers]
print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Squares of the list elements:", squares)
