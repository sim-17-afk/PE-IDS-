# Assignment 6: Implementation of Universal Functions in NumPy

import numpy as np

# Create sample arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Arithmetic ufuncs
print("\n--- Arithmetic Universal Functions ---")
print("Addition:", np.add(arr1, arr2))         # element-wise addition
print("Subtraction:", np.subtract(arr2, arr1)) # element-wise subtraction
print("Multiplication:", np.multiply(arr1, arr2)) 
print("Division:", np.divide(arr2, arr1))

# Power, Mod, Reciprocal
print("\n--- More Universal Functions ---")
print("Power:", np.power(arr1, 2))     # arr1^2
print("Modulus:", np.mod(arr2, arr1))  # arr2 % arr1
print("Reciprocal:", np.reciprocal(arr1))

# Trigonometric functions
print("\n--- Trigonometric Universal Functions ---")
print("Sine:", np.sin(arr1))
print("Cosine:", np.cos(arr1))
print("Tangent:", np.tan(arr1))

# Exponential and Logarithmic functions
print("\n--- Exponential & Log Universal Functions ---")
print("Exponential:", np.exp(arr1))
print("Natural Log:", np.log(arr1))     # log base e
print("Log base 10:", np.log10(arr1))

