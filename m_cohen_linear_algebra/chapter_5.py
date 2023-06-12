#5.12: Coding challenge

# 1. Create a matrix that contains the dot product between all pairs of columns in two other matrices.
# two 4x2 matrices of random number, double for loop for dot product between each column.

import numpy as np
from typing import List

A = np.random.rand(4,2)
B = np.random.rand(4,2)

C = np.zeros((2,2))
for i in range(A.shape[1]):
    for j in range(B.shape[1]):
        C[i,j] = np.dot(A[:,i], B[:,j])

# 2. Create symmetric matrix from random -> convert to triangular, transpose and matrix addition

A = np.random.rand(4,4)
symmetric = np.tril(A) + (np.tril(A).T)

# 3. create a diagonal matrix of 4x8 without using diag() function, diag element should be 1,2,3,4
def diagonal_matrix(r:int,c:int, elements: List[int]):
    # only numbers if r == c, else 0
    matrix = np.zeros((r,c))
    if c < r : 
        raise ValueError('number of columns must exceed rows')
    for i in range(r):
        matrix[i,i] = elements[i]
    
    return matrix
