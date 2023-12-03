import numpy as np
import sympy as sym

# Create vector that contains the values of the variables
x = np.random.rand(3)

# make up the expression with random coefficients
# 3x + 4y - 2z
A = np.random.randint(5, size=(3,3))

# solution is A@x
y = A @ x

# create random numbers matrices that are (1) square, (2) wide, or (3) tall; 
# and then compute and examine the RREF of those matrices.

square_matrix = np.random.rand(3,3)
square_rref = sym.Matrix(square_matrix).rref()

wide_matrix = np.random.rand(3,9)
wide_rref = sym.Matrix(wide_matrix).rref()

tall_matrix = np.random.rand(9,3)
tall_rref = sym.Matrix(tall_matrix).rref()