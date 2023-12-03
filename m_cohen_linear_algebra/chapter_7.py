
# question 1 
# create random matrices with any arbitary rank
# since we know that random matrices are most likely full rank
# combined with the fact that the maximum rank for a matrix is the smallest dimension for the multiplied matrices.
import numpy as np

def random_rank(rank:int)->np.ndarray:
    random_matrix = np.random.rand(rank + 1, rank)

    return random_matrix @ random_matrix.T

assert np.linalg.matrix_rank(random_rank(3)) == 3

assert np.linalg.matrix_rank(random_rank(88)) == 88

# question 2
# machine epsilon: print(np.finfo(np.float64).eps)
machine_epsilon = np.finfo(np.float64).eps

A = np.zeros((5,5))

assert np.linalg.matrix_rank(A) == 0
assert np.linalg.matrix_rank(A + (np.random.rand(5,5) * machine_epsilon)) == 5

assert np.linalg.matrix_rank(A + (np.random.rand(5,5) * (machine_epsilon * 1e-8807))) == 0
print(np.linalg.norm(A + (np.random.rand(5,5) * (machine_epsilon * 1e-8807)), 'fro'))