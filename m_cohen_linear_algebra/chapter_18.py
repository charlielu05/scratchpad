# implement equations 18.10 and 18.13
# create a data matrix of random numbers with 4 features and 200 observations.
# compute the correlation and covariance matrices using the equations above.
# confirm results with Python packages
import numpy as np

x_1 = np.random.rand(200)
x_2 = x_1 * 1.5 + 8
x_3 = np.random.rand(200)
x_4 = x_3 * 1.2 + x_2 * 4

X = np.array([x_1, x_2, x_3, x_4]).T

# mean centre
X_mean = np.mean(X, axis=0)

# broadcasted
X_mean_centred = X - X_mean

# equation 18.10, R=S^-1 @ X.T @ X @ S^-1
std = np.std(X_mean_centred, axis=0, ddof=1)
S = np.diag(std)
C = np.linalg.inv(S) @ X_mean_centred.T @ X_mean_centred @ np.linalg.inv(S)
R = C @ np.diag([1 / 199] * 4)

assert np.isclose(np.corrcoef(X.T), R).all()

# covariance from correlation
C_derived = S @ R @ S

assert np.isclose(np.cov(X.T), C_derived).all()
