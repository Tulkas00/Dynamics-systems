import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(x, a, b):
    return -b * x + b - a

# Define the Chua's circuit system of ODEs
def chua_circuit(y, t, gamma, beta, a, b):
    y1, y2, y3 = y
    dy1 = gamma * (y2 - y1 - f(y1, a, b))
    dy2 = y1 - y2 + y3
    dy3 = -beta * y2
    return [dy1, dy2, dy3]

# Parameters
gamma = 10
beta = 18.36
a = -1.38
b = -0.74

# Initial conditions
y0 = [0.7, 0, 0]

# Time vector
t = np.linspace(0, 200, 20001)

# Solve the system of ODEs
z = odeint(chua_circuit, y0, t, args=(gamma, beta, a, b))

# Plot the results
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(z[:, 0], z[:, 1], z[:, 2], linewidth=1)
ax.set_xlabel("y1")
ax.set_ylabel("y2")
ax.set_zlabel("y3")
ax.set_title("Chua Circuit Trajectory")
plt.show()
