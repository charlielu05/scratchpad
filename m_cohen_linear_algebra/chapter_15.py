import numpy as np
from scipy.linalg import eig

# question 1
# two matrices A and B
# perform generalised eigendecomposition on both matrices
# perform regular eigendecomposition on the matrix B^-1A
# inspect whether the eigenvalues are the same
A = np.random.rand(2, 2)
B = np.random.rand(2, 2)

first_method = eig(A, B)
second_method = np.linalg.eig(np.linalg.inv(B) @ A)
A_approx = (
    B @ first_method[1] @ (np.diag(first_method[0])) @ np.linalg.inv(first_method[1])
)

# question 2
# diagonalization means to transform matrix into a diagonal matrix
# eigenvectors provides the transformational matrix.
# what happens if A is already a diagonal matrix? what are its eigenvalues and eigenvectors

C = np.diag(np.random.rand(3))
D = np.triu(np.random.rand(3, 3))
D_eigvalues, D_eigvectors = np.linalg.eig(D)

# question 3
# create a 50x50 Hankel matrix and take its eigendecomposition
# sort the eigenvectors according to descending eigenvalues
