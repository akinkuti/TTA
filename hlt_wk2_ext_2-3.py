#In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) 
# – remove all repeating items present in array b
import numpy as np

#array_a defined
array_a = np.array([1,2,3,4,5])
print("This is array_a: ", array_a,"\n")

#array_b defined
array_b = np.array([4,5,6,7,8,9])
print("This is array_b: ", array_b,"\n" )


#array_b now array_b-new without repeating items in array_a using np.setdiff1d
array_b_new = np.setdiff1d(array_b, array_a)
print("This is array_b_new without repeating elements in array-a:\n", array_b_new, "\n")

#For array_a and array_b combined
#Get all items between 3 and 7 from a and b and sum them together

#array_a and array_b Concatenated:
combined_array = np.concatenate((array_a, array_b))
print("This is array_a and array_b combined:\n", combined_array,"\n" )

#Find elements in range 3 to 7
result_3_7 = combined_array[(combined_array>=3)*(combined_array<=7)]
print("Resultant array that contains only integers 3 - 7 : ", result_3_7, "\n")

#Sum of elements with numeric values between 3-7
sum_result_3_7 = np.sum(result_3_7)
print("This is the sum of integers with values 3 - 7 within the array: ", sum_result_3_7)