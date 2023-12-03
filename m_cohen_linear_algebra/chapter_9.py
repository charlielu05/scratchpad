import numpy as np

# confirm unitary matrix on p.252 is indeed unitary
unitary_matrix = (1/2) * np.matrix([[1 + 1j, 1 - 1j],
                                    [1 - 1j, 1 + 1j]])

# confirm that the hermitian transpose of U multiplied by U is unity
print(unitary_matrix.H @ unitary_matrix)

# confirm that the transpose of U multiplied by U is not unity
print(unitary_matrix.T @ unitary_matrix)

# two methods to produce symmetric matrices, A.T @ A and A + A.T
A1 = unitary_matrix.H @ unitary_matrix
A2 = unitary_matrix + unitary_matrix.H