import numpy as np
from numpy import linalg

if __name__ == "__main__":
    # Write code that illustrates eq 11.26
    # generate 4x4 matrix A with integers between 0 and 10 
    # then generate random integers B between -10 and -1
    # print out the left and right hand side of eq 11.26
    # det(BA) = B * det(A)

    A = np.random.randint(0,10, (4,4))
    B = np.random.randint(-10, -1, 1)

    c = linalg.det(B * A)

    d = np.power(B, 4)

    e = d * linalg.det(A)

    assert np.isclose(c, e[0])

    