'''
Rayaan Hassan
Spring 2026
CMSC 111
Week 13 Assignment 1
Code Helped - Gemini Google AI
'''

import numpy as np

# Task 1: Create a NumPy Array containing 1 through 100
# np.arange(start, stop) goes up to but NOT including the stop number
arr = np.arange(1, 101)
print("Original Array:\n", arr)

# Task 2: Reshape the array into a 10 x 10 matrix
matrix = arr.reshape(10, 10)
print("\n10x10 Matrix:\n", matrix)

# Task 3: Extract specific rows 5 through 8
# Remember: Zero-based indexing means Row 5 is index 4.
# Slicing [4:8] includes indices 4, 5, 6, and 7 (Rows 5, 6, 7, 8).
rows_5_to_8 = matrix[4:8]
print("\nRows 5 through 8:\n", rows_5_to_8)

# Task 4: Compute the sum of all elements
total_sum = np.sum(matrix)
print("\nSum of all elements:", total_sum)