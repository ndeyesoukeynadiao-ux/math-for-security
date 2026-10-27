"""
Math for Security - Exercise 01
Topic: Matrix Operations & Determinants (Linear Algebra)
Objective: Solve by hand, then verify using Python for Cloud Security & Cryptography foundations.
"""

import numpy as np

# 1. Define matrices
A = np.array([[2, 3], 
              [1, 4]])

B = np.array([[5, 1], 
              [0, 2]])

# 2. Matrix Multiplication (A * B)
product = np.dot(A, B)
print("Product A * B:\n", product)

# 3. Matrix Determinant det(A)
det_A = np.linalg.det(A)
print("\nDeterminant of A:", round(det_A, 2))

# 4. Inverse of Matrix A
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
else:
    print("\nMatrix A is singular (non-invertible).")
