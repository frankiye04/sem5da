# ex1.py
import functools
import pandas as pd
numbers = [1, 5, 7, 8, 9]
doubled_numbers = list(map(lambda x: x * 2, numbers))
sum_of_numbers = functools.reduce(lambda x, y: x + y, numbers)
print("Original list:", numbers)
print("Doubled list:", doubled_numbers)
print("Sum of original list:", sum_of_numbers)
