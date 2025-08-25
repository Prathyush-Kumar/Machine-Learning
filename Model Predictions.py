import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
x = 2 * np.random.random((100, 1))
y = 4 + 3 * x + np.random.randn(100, 1)

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

plt.scatter(x, y, color="blue", label="Data Points")
plt.plot(x, y_pred, color="red", linewidth=2, label="Predictions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
