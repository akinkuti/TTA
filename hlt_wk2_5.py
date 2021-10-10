# Convert a 1D array to a 2D array with 2 rows

#Create a 1D array with 12 elements
import numpy as np
array_1D_elements = np.arange(1, 13)
print("This is a 1D array of 12 elements: ", array_1D_elements)

#Convert above 1D array to 2D
array_2D = np.reshape(array_1D_elements, (2, 6))
print("This is a 2D array with 2 rows:  \n", array_2D)


