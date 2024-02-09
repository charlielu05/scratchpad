# Explore definiteness of random-integer matrices.
# Generate a 4x4 matrix of random integers between -10 and +10, all real-valued eigenvalues.
# Possible by multiplying the matrix by its transpose.
# Once this works, compute the definiteness category of that matrix

# Embed inside a for-loop to generate 500 matrices. Store the definiteness category for each matrix.

import numpy as np


def generate_random_matrix():
    return np.random.randint(-10, 10, size=(4, 4))


def find_positive_eig_value_matrix():
    is_positive_eig = False

    while is_positive_eig != True:
        random_matrix = generate_random_matrix()
        e_value, _ = np.linalg.eig(random_matrix)
        if np.iscomplex(e_value).any() == True:
            is_positive_eig == False
        else:
            break

    return random_matrix


def definiteness_category(matrix) -> str:
    e_value, eig_vector = np.linalg.eig(matrix)

    # positive definite, all positive eig_values
    if all(val > 0 for val in e_value):
        return "positive definite"

    # positive eigenvalues and 0
    elif all(val >= 0 for val in e_value):
        return "positive semidefinite"

    elif all(val <= 0 for val in e_value):
        return "negative semidefinite"

    elif all(val < 0 for val in e_value):
        return "negative definite"

    else:
        return "indefinite"


# generate random matrix between -10 and +10
if __name__ == "__main__":
    positive_eig_arrays = [find_positive_eig_value_matrix() for i in range(500)]
    definiteness = [definiteness_category(x) for x in positive_eig_arrays]
    print(definiteness.count("positive definite"))
    print(definiteness.count("positive semidefinite"))
    print(definiteness.count("indefinite"))
