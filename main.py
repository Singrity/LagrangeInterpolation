
import numpy as np
import matplotlib.pyplot as plt

X = []

Y = []


with open("x_data.txt", 'r') as file:
    x_data = file.read().split("\n")

for i, x in enumerate(x_data):
    x_data[i] = float(x)
    X.append(x_data[i])


with open("y_data.txt", 'r') as file2:
    y_data = file2.read().split("\n")

for i, y in enumerate(y_data):
    y_data[i] = float(y)
    Y.append(y_data[i])

#print(f"{X}\n{Y}")


def basics(ab, j):
    p = [(ab - X[m]) / (X[j] - X[m]) for m in range(len(X)) if m != j]
    return np.prod(p, axis=0) * Y[j]


def interpolate(ab):
    p = [basics(ab, j) for j in range(len(X))]
    return np.sum(p, axis=0)


ab = np.arange(-10, 10)

plt.plot(ab, interpolate(ab))
plt.show()
