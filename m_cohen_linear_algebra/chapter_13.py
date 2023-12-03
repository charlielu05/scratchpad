import numpy as np


# generate random matrix of size M, N. they are generally full rank
def full_rank_matrix(m: int, n: int):
    return np.random.rand(m, n)


if __name__ == "__main__":
    # Question 1
    # use code to confirm size of Q and R matrix when QR decomposition is used

    # square full rank
    Q, R = np.linalg.qr(full_rank_matrix(3, 3))
    assert Q.shape[0] == Q.shape[1]
    assert R.shape[0] == R.shape[1]

    # tall "full" QR
    A = full_rank_matrix(9, 3)
    Q, R = np.linalg.qr(A, mode="complete")
    assert (Q.shape[0] and Q.shape[1]) == A.shape[0]
    assert (Q.shape[0] and Q.shape[1]) != A.shape[1]
    assert R.shape == A.shape

    # tall "enconomy" QR
    A = full_rank_matrix(9, 3)
    Q, R = np.linalg.qr(A, mode="reduced")
    assert Q.shape[1] == A.shape[1]
    assert A.shape != R.shape

    # wide QR
    A = full_rank_matrix(3, 9)
    Q, R = np.linalg.qr(A, mode="reduced")
    assert (Q.shape[0] and Q.shape[1]) == A.shape[0]
    assert R.shape[0] < R.shape[1]

    # Question 2
    # implement the Gram-Schmidt algorithm
    def vector_proj(v1, v2):
        return (v2.T @ v1) / (v1.T @ v1) * v1

    def gs(A):
        Q = np.zeros((A.shape))

        # loop through columns
        for i in range(A.shape[1]):
            Q[:, i] = A[:, i]

            a = A[:, i]
            for j in range(i):
                q = Q[:, j]
                Q[:, i] = Q[:, i] - vector_proj(q, a)
            Q[:, i] = Q[:, i] / np.linalg.norm(Q[:, i])
        return Q

    A = full_rank_matrix(4, 4)
    Q = gs(A)
