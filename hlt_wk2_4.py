#Replace all odd numbers in an array of 1-10 with the value -1

import numpy as np

#create array of 1-10
number_to_ten = np.arange(1, 11)
print("Numbers from 1-10 :             ", number_to_ten)

#To identify the odd numbers in the array and replace with -1
odd_number = (number_to_ten%2 == 1) 
number_to_ten[odd_number] = -1 
print("Odd Number replace by -1 :      ", number_to_ten)                  
