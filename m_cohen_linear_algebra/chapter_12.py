import numpy as np
from numpy.linalg import det

# implement the MCA algorithm
# Compute minors matrix
# Compute cofactors matrix
# Compute the adjucate matrix


def minors_matrix(X):
    # determinant of the matrix, where each element excludes the current x,y index of the cell
    # loop through matrix
    minors = np.zeros(X.shape)

    for n in range(X.shape[1]):
        for m in range(X.shape[0]):
            # exclude index row
            Y = np.delete(X, m, 0)
            # exluce index column
            Y = np.delete(Y, n, 1)

            minors[m, n] = det(Y)

    return minors


def cofactors_matrix(X):
    # create alternating signs matrix G
    G = np.zeros(X.shape)

    # odd number rows
    for m in range(G.shape[0]):
        if m % 2 == 0:
            G[m, ::2] = 1
            G[m, 1::2] = -1
        else:
            G[m, ::2] = -1
            G[m, 1::2] = 1

    return np.multiply(X, G)


def adjucate_matrix(X, determinant):
    # transpose of the cofactors matrix, scalar multiplied by the inverse of the determinant of the original matrix
    return np.multiply(X.T, determinant)


def mca(X):
    determinant = np.linalg.det(X)
    return adjucate_matrix(cofactors_matrix(minors_matrix(X)), determinant)


if __name__ == "__main__":
    # create some test matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[4, 3], [2, 1]])

    np.testing.assert_allclose(minors_matrix(A), B)

    C = np.array([[3, 4, 1], [0, 2, 3], [5, 4, 1]])
    D = np.array([[-10, -15, -10], [0, -2, -8], [10, 9, 6]])

    np.testing.assert_allclose(minors_matrix(C), D)

    # Cofactors matrix
    E = np.array([[1, 2], [3, 4]])
    F = np.array([[4, -3], [-2, 1]])
    np.testing.assert_allclose(cofactors_matrix(minors_matrix(E)), F)

    # Adjugate matrix
    G = np.array([[1, 1], [1, 4]])
    H = np.array([[12, -3], [-3, 3]])
    np.testing.assert_allclose(mca(G), H)

    # test the MP inverse
    # np.linalg.pinv

    # test that the MP inverse is the same as the real inverse for a full rank square matrix
    square_full_rank = np.random.rand(3, 3)
    np.testing.assert_allclose(
        np.linalg.pinv(square_full_rank), np.linalg.inv(square_full_rank)
    )
    tall_full_rank = np.random.rand(10, 3)
    left_inverse = np.linalg.inv(tall_full_rank.T @ tall_full_rank) @ tall_full_rank.T
    mp_left_inverse = np.linalg.pinv(tall_full_rank)
    np.testing.assert_allclose(left_inverse, mp_left_inverse)
