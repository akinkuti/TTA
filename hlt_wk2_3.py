#Extract all odd numbers from array of 1-10

import numpy as np

#To creat array of numbers from 1-10
array_of_ten = np.arange(1, 11)
print("array of numbers 1-10: ",             array_of_ten)

#To extract all odd numbers from above array
odd_numbers  = array_of_ten[0::2]
print("odd number extract from the array: ", odd_numbers)