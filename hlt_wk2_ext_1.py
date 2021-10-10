# Create two arrays a and b, stack these two arrays vertically use the np.dot and 
#np.sum to calculate totals

import numpy as np
#To create array for 111
array_111 = np.array([1,1,1])
print(array_111)

#To create array for 222
array_222 =np.array([2,2,2])
print(array_222)  

#To create array for 333
array_333 = np.array([3,3,3])
print(array_333)

#To create array for 123
array_123 = np.array([1,2,3])
print(array_123)

#To create array to combine the sub arrays
overall_array = np.concatenate((array_111, array_222, array_333, array_123, array_123, array_123))
print(overall_array)