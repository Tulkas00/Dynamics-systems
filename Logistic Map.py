import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_values = np.linspace(2.5, 4.0, 10000)  # Range of r
n_iterations = 1000  # Number of iterations
last = 100  # Last iterations to plot (to show long-term behavior)

# Prepare the bifurcation diagram
x = 1e-5 * np.ones(len(r_values))  # Initial condition for x

# Create the bifurcation diagram
for _ in range(n_iterations):
    x = r_values * x * (1 - x)
    if _ >= (n_iterations - last):  # Only plot the last iterations
        plt.plot(r_values, x, ',k', alpha=0.25)

# Plot formatting
plt.title("Bifurcation Diagram of Logistic Map")
plt.xlabel("Growth rate (r)")
plt.ylabel("Population (x)")
plt.show()
