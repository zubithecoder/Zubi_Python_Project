import numpy as np 

lst = [1, 2, 3, 4, 5]
arr = np.array(lst) 
print(arr)

# All zeros array
arr_zeros = np.zeros((3, 4)) # 3 rows, 4 columns
print(arr_zeros) 

# All ones array
arr_ones = np.ones((2, 5)) # 2 rows, 5 columns
print(arr_ones)

# Array with a range of values
arr_range = np.arange(1, 11, 2) # Start at 1, end before 11, step by 2
print(arr_range)

# Array Attributes
print("Array Shape:", arr_zeros.shape) # Shape of the array
print("Array Data Type:", arr_zeros.dtype) # Data type of the array elements
print("Array Size:", arr_zeros.size) # Total number of elements in the array
print("Array Dimensions:", arr_zeros.ndim) # Number of dimensions

# Multi-Dimensional Arrays
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print(matrix[0, 1]) # Accessing element at row 0, column 1
print(matrix[:, 2]) # Accessing all rows in column 1

# Arrays Operations
print("Array Operations:")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Addition:\n", arr1 + arr2)  # Element-wise addition
print("Subtraction:\n", arr1 - arr2)  # Element-wise subtraction
print("Multiplication:\n", arr1 * arr2)  # Element-wise multiplication
print("Division:\n", arr1 / arr2)  # Element-wise division

# Reshaping Arrays
print("Reshaping Arrays:")
arr_reshaped = arr1.reshape((4, 1)) # Reshape to 4 rows, 1 column
print("Original Array:\n", arr1)
print("Reshaped Array:\n", arr_reshaped)

""" Practice Problems: """
# 1. Create a NumPy array of numbers from 10 to 30 with step size 2.
# Creating array from 10 to 30 with step size 2
arr_practical = np.arange(10, 31, 2)
print(arr_practical)

# 2.  Create a 2D array with 2 rows and 3 columns filled with ones.
# Creating a 2D array with 2 rows and 3 columns filled with ones
arr_ones_2D = np.ones((2, 3))
print(arr_ones_2D)

# 3. Perform element-wise multiplication on two arrays.
# Define two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
# Element-wise multiplication
result = array1 * array2
print(result)

# 4. Reshape an array of 16 elements into a 4x4 matrix.
# Create an array of 16 elements (0 to 15)
array_16 = np.arange(16)
# Reshape into a 4x4 matrix
matrix_4x4 = array_16.reshape((4, 4))
print(matrix_4x4)

 # ------------------------------------------------ 
