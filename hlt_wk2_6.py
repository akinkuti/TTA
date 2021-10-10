# Create two arrays a and b, stack these two arrays vertically use the np.dot and 
#np.sum to calculate totals
import numpy as np

#To create first array (array_a) of 3X3 using numbers starting from 20
array_a = np.arange(20, 29).reshape(3,3)
print("This ia the 1st array for manipulation: \n" , array_a)


#To create second array (array_b) of 3X3 using numbers starting from 40
array_b = np.arange(40, 49).reshape(3,3)
print("This is the 2nd array for manipulation: \n" , array_b)

#Manipulation of Both array_a and array_b 
array_a_b = np.dot(array_a, array_b)
print("This is the matrix multiplication for both arrays:\n ", array_a_b)

total_sum_a_b = np.sum(array_a_b, axis = 0)
print("Total sum for manipulation: ", total_sum_a_b)
