from chapter_7 import random_rank
from scipy.linalg import null_space
import numpy as np

# Question 1 
# Create two 4×4 random numbers matrices, 
# each with rank = 3 (consult the code challenge from Chapter 7 for how to do this). 
# Call those matrices A and B. Then find a vector in the null space of A(vector n). 
# Finally, show that BAn is the zeros vector while ABn is not .

A = random_rank(3) 
B = random_rank(3)

# vector in null space of A
z = null_space(A)

# check that z is indeed a vector in the null-space of A
assert np.isclose(A @ z, 0).all()
# check that BAz is 0
assert np.isclose(B @ A @ z, 0).all()
# check that ABz is not 0
assert not np.isclose(A @ B @ z, 0).all()

# Question 2 
# Create a 16×11 matrix with rank=9. 
# Then identify bases for the left- and right-null spaces and determine their dimensionalities.
# Confirm that the dimensionality of the left-null space plus the dimensionality of the column space is 16 (the ambient dimensionality of the column space), 
# and that the dimensionality of the null space plus the dimensionality of the row space is 11

# create random matrix with rank 9
A = random_rank(9)
B = np.append(A, A[:6:], 0)
C = np.append(B, B[:,[0]], 1)

assert np.linalg.matrix_rank(A) == 9
assert np.linalg.matrix_rank(B) == 9
assert np.linalg.matrix_rank(C) == 9

# rank is equivalent to row and column space
r = np. linalg .matrix_rank(C)

# left null space
left_null = null_space(C.T)

# right null space
right_null = null_space(C)
