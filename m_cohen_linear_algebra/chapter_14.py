import numpy as np

# data is in sales.txt
# time of sale, age of buyer, number of widgets sold

# 1 . Explain and write the mathematical model that is appropriate for this dataset
# linear regression, time of sale * B1 + age of buyer * B2 = number of widgets sold

# 2. Write the matrix equation corresponding to the model
# Design matrix column 1 and 2 consists of time of sale and age of buyer
# design @ [b1 b2].T = widgets sold

# 3. Compute the model coefficients using the least squares algorithm
# beta = (X.T @ X)^-1 @ X.T @ y
data = np.loadtxt("./sales.txt", delimiter=",")
X = np.concatenate((np.ones((1000, 1)), data[:, :2]), axis=1)
y = data[:, -1].reshape(-1, 1)

B = np.linalg.inv(X.T @ X) @ X.T @ y

y_hat = X @ B

y_error = y - y_hat

# 5. Calculate R^2 value and see how well the model fits the data
# R^2 = 1 - (sum of residuals squared) / (sum of (y - y_average)^2)

residuals_squared = y_error.T @ y_error
y_avg = np.mean(y)
y_avg_removed = y - y_avg
y_avg_removed_squared = y_avg_removed.T @ y_avg_removed

r_squared = 1 - (residuals_squared / y_avg_removed_squared)
