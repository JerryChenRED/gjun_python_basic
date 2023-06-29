from lesson_fibonacci_function import find_fibonacci
from lesson_gcd_function import find_great_common_divisors
import math
import numpy as np 


print("hello")

n = 2 
numbers = np.random.choice(1000, n, replace=False)
print("Numbers: ", numbers, math.gcd(*numbers))
result = find_great_common_divisors(numbers)
print(result)