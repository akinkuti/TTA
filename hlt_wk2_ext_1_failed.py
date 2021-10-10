# Create the following pattern without hardcoding. Use only NumPy functions
#Array to be created ([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3])
import numpy as np
#Create array of 1s with three elements
array_111 = np.ones(3)
print(array_111)

#Create an array consisting of [1,2,3]
array_123 = np.arange(1,4)
print(array_123)

#Create an array for [2,2,2]
array_222 = array_111 * 2
print(array_222)

#Create an array for [3,3,3]
array_333 = array_111 * 3
print(array_333)

#Concatenating of above arrays to get desired result
#final_array = np.concatenate((array_111), (array_111))
#print(final_array)