import numpy as np
import array  

# Array Broadcasting
arr1 = np.array([1,2,3])
arr2 = np.array((2,))
arr3 = arr1 + arr2  # Broadcasting will add 2 to each element of aar1
print(arr3) 


# Example of Broadcasting with 2D arrays
data = np.array([[160, 60], [170, 70], [180, 80]])  # height, weight
scale_factor = np.array([0.01, 1])  # scale factor for height and weight
scale_data = data * scale_factor  # Broadcasting will apply of scale factor to each row (scale the data)
print("Scaled Data:\n", scale_data) 


# Vectorized Operations
array = np.array([1, 2, 3, 4, 5])
squared_array = array ** 2  # Squaring each element in the array
print("Squared Array:", squared_array) 


# Linear Algebra Using linalg Module
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)  # Matrix multiplication
""" Perform matrix multiplication using np.dot()
 This multiplies the rows of 'a' with the columns of 'b'
"""
"""
It will gonna multiply like this: 
(1*5 + 2*7) : 5 + 14 = 19
(1*6 + 2*8) : 6 + 16 = 22
(3*5 + 4*7) : 15 + 28 = 43
(3*6 + 4*8) : 18 + 32 = 50
"""
print("Matrix Multiplication Result:\n", result)

# Inverse of a Matrix
inverse_a = np.linalg.inv(a)
"""
How inverse works (for a 2x2 matrix):

If we have a = [[a, b],
                [c, d]]

Then the formula for the inverse is:
(1 / (a*d - b*c)) * [[ d, -b],
                      [-c,  a]]

Let's apply that here:
a = 1, b = 2, c = 3, d = 4

determinant = (1*4 - 2*3) = 4 - 6 = -2

Now multiply (1/det) = -1/2 with:
[[ 4, -2],
 [-3,  1]]

So the inverse is:
= [[-2.0,  1.0],
   [ 1.5, -0.5]]
"""
print("Inverse of Matrix a:\n", inverse_a)
"""
Short notes to remember (so you can read code later)
np.linalg.inv(x) → returns inverse of matrix x.
np.dot(A, B) or A @ B → matrix multiplication.
determinant = a*d - b*c for 2*2 → if determinant == 0 → no inverse.
Determinant ≠ 0 → Inverse exists
Determinant = 0 → Matrix has no inverse
"""


# Determinant of a Matrix
det_a = np.linalg.det(a)
print("Determinant of Matrix a:\n", det_a)  # Output: -2.0


# Eigenvalues and Eigenvectors
eigenvalues, eigenvactors = np.linalg.eig(a)
print("Eigenvalues of Matrix a:\n", eigenvalues)
"""
Eigenvalues → how much matrix stretches or shrinks
Eigenvectors → directions that don't change (only scaled)
"""


