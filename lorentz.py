import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz system
def lorenz_system(state, t, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parameters for the Lorenz system
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Initial conditions
initial_state = [1.0, 1.0, 1.0]

# Time vector
t = np.linspace(0, 50, 10000)

# Solve the system using odeint
from scipy.integrate import odeint
trajectory = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))

# Extract X, Y, Z coordinates
x, y, z = trajectory[:, 0], trajectory[:, 1], trajectory[:, 2]

# Plot the trajectory
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='blue', linewidth=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor")
plt.show()
