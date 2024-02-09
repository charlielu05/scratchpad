from numpy import linalg
import numpy as np
import requests
from PIL import Image
import io

# Chapter 16: Singular Value Decomposition

# Question 1
# Economy QR decomposition, can be useful for large tall matrices. There is also an "enconomy" version of the SVD.
# Goal is to find what that means
# Generate three random matrices: square, wide and tall, run full SVD to confirm the sizes of the SVD matrices match with expectations.
# Finally run the economy SVD and compare the size to the full SVD.

square, wide, tall = np.random.randn(3, 3), np.random.randn(3, 6), np.random.randn(6, 3)

# Full SVD
square_svd, wide_svd, tall_svd = linalg.svd(square), linalg.svd(wide), linalg.svd(tall)

# mapping from int to string
svd_mapping = {0: "U", 1: "S", 2: "V"}

for i in range(3):
    print(f"Square {svd_mapping.get(i)}: {square_svd[i].shape}")
    print(f"Wide {svd_mapping.get(i)}: {wide_svd[i].shape}")
    print(f"Tall {svd_mapping.get(i)}: {tall_svd[i].shape}")

# Economy SVD
eco_square_svd, eco_wide_svd, eco_tall_svd = (
    linalg.svd(square, full_matrices=False),
    linalg.svd(wide, full_matrices=False),
    linalg.svd(tall, full_matrices=False),
)

for i in range(3):
    print(f"Eco Square {svd_mapping.get(i)}: {eco_square_svd[i].shape}")
    print(f"Eco Wide {svd_mapping.get(i)}: {eco_wide_svd[i].shape}")
    print(f"Eco Tall {svd_mapping.get(i)}: {eco_tall_svd[i].shape}")

# Question 2
# Obtain the three SVD matrices from eigendecomposition of the covariance matrix of the data matrix X
# Compare the results to the SVD of X

X = np.random.randn(3, 6)

# eigen decomposition of covariance matrix
# get U
eig_vals_U, eig_vecs_U = linalg.eig(X @ X.T)
U = eig_vecs_U[:, np.argsort(eig_vals_U)[::-1]]
eig_vals_V, eig_vecs_V = linalg.eig(X.T @ X)
V = eig_vecs_V[:, np.argsort(eig_vals_V)[::-1]]

# SVD of X
X_svd = linalg.svd(X)

# assert that the SVD matrices and the eigen decomposition matrices are the same/close enough
assert np.isclose(abs(U), abs(X_svd[0])).all()
# assert np.isclose(abs(V), abs(X_svd[2].T)).all()

# Question 3
# Write code to reproduce panels B and C in Figure 16.5
# Confirm that the reconstructed matrix is equal to the original matrix
# SVD spectral theory
A = np.random.randn(5, 3)
A_u, A_s, A_v = linalg.svd(A)

u_1 = A_u[::, 0].reshape(-1, 1)
s_1 = A_s[0].reshape(-1, 1)
v_1 = A_v[0, ::].reshape(-1, 1)

spectral_1 = np.outer(u_1, (s_1 @ v_1.T))

u_2 = A_u[::, 1].reshape(-1, 1)
s_2 = A_s[1].reshape(-1, 1)
v_2 = A_v[1, ::].reshape(-1, 1)

spectral_2 = np.outer(u_2, (s_2 @ v_2.T))

u_3 = A_u[::, 2].reshape(-1, 1)
s_3 = A_s[2].reshape(-1, 1)
v_3 = A_v[2, ::].reshape(-1, 1)

spectral_3 = np.outer(u_3, (s_3 @ v_3.T))

total_spectral = spectral_1 + spectral_2 + spectral_3

# Question 4
# Create a random numbers matrix with a specified condition number
# condition number = ratio of largest to smallest singular value

m = 6
n = 16
condition = 42.0

U = np.linalg.qr(np.random.randn(m, m))[0]
V = np.linalg.qr(np.random.randn(n, n))[0]
s = np.linspace(condition, 1, np.min((m, n)))
S = np.zeros((m, n))
for x, i in enumerate(s):
    S[x, x] = i

created_cond_matrix = U @ S @ V.T
created_cond_matrix_number = np.linalg.cond(created_cond_matrix)

# Question 5
# Create SVD of a picture

# download picture

IMAGE_URL = "https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg"
picture_content = requests.get(IMAGE_URL).content
img = Image.open(io.BytesIO(picture_content))
arr = np.asarray(img)

U, S, V = np.linalg.svd(arr)

# Question 6
# Create a scree plot of the percent normalized singular values.
# then test various thresholds for reconstructing the picture
# including all components that explain at least 4% of the variance
S_norm = (100 * S) / sum(S)

# Question 7
# Compute the error between the reconstruction and the original image.
# RMS (root mean squared error)
rms = np.zeros(len(S_norm))

S_img = np.zeros(arr.shape)

for x, i in enumerate(S):
    S_img[x, x] = i

for si in range(len(S_norm)):
    i = si + 1  # mind the indexing!
    lowrank = U[:, :i] @ S_img[:i, :i] @ V[:i, :]
    diffimg = lowrank - arr
    rms[si] = np.sqrt(np.mean(diffimg.flatten() ** 2))

# Question 8, what is the pseudo inverse of a column vector of constants?
X = np.random.randint(low=1, high=7, size=(4, 2))
