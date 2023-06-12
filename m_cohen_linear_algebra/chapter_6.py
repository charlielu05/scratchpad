import numpy as np
from typing import List

# Implement matrix multiplication between a 2×4 matrix and a 4×3 matrix, 
# using the "layer perspective" in a for-loop. 
# Confirm that you get the same result as when you compute matrix multiplication using @ (Python) or * (MATLAB).

def matrix_multiply(a:np.array, b:np.array)->np.array:
    # assert shape is valid
    assert len(set([len(x) for x in b])) == 1
    assert a.shape[1] == b.shape[0]
    
    result_matrix = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[1]):
        result_matrix += np.outer(a[:, i], b[i, :])
        
    return result_matrix

A = np.random.randn(2,4)
B = np.random.randn(4,3)

assert np.allclose(A@B, matrix_multiply(A,B)) == True

# Generate a 4 × 4 diagonal matrix and a 4 × 4 dense matrix of random numbers. 
# Compute both standard and Hadamard multiplication between them. 
# You already know that the re- sulting product matrices are not the same, but what about the diagonals of those two product matrices?

diagonal_matrix = np.diag(np.array([1,2,3,4]))
dense_matrix = np.random.randn(4,4)

standard_multiply = diagonal_matrix @ dense_matrix
hadamard_multiply = np.multiply(diagonal_matrix, dense_matrix)

assert (np.diag(standard_multiply) == np.diag(hadamard_multiply)).all() 

# Consider C1 = (AT + A)/2 and C2 = ATA for some square
# nonsymmetric matrix A. C1 and C2 are both symmetric and
# both formed from the same matrix, yet in general C1 ̸= C2.
# Interestingly, if A is a diagonal matrix with all non-negative
# values, then C1 = C1/2. Show this in code using random 2
# numbers, and then explain why you get this result.

A = np.random.randn(4,4)
C1 = (A.T + A) / 2
C2 = A.T@A

# check symmetry
assert (C1.T == C1).all()
assert (C2.T == C2).all()

A2 = np.diag(np.random.randn(4))
C1 = (A2.T + A2) / 2
C2 = A2.T@A2

assert np.allclose(abs(np.power(C2, .5)), abs(C1)) == True

# Let’s explore the Cauchy-Schwarz inequality. 
# Generate a ran-dom matrix A and a random vector v, compute the norms of both sides of the inequality 6.27 (page 168), 
# and show that the right-hand side is larger than the left-hand side.

A = np.random.randn(4,3)
v = np.random.randn(3)

assert np.linalg.norm(A@v, 2) <= np.linalg.norm(A, 'fro') * np.linalg.norm(v, 2)