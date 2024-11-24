import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the Van der Pol Oscillator ODE
def van_der_pol(y, t, mu):
    x, dxdt = y
    dydt = [dxdt, mu * (1 - x**2) * dxdt - x]
    return dydt

# Parameters
mu = 1.0  # Nonlinearity parameter
y0 = [1.0, 0.0]  # Initial conditions [x(0), dx/dt(0)]
t = np.linspace(0, 50, 1000)  # Time array

# Solve the ODE
solution = odeint(van_der_pol, y0, t, args=(mu,))
x = solution[:, 0]  # x(t)
dxdt = solution[:, 1]  # dx/dt(t)

# Plot the results
plt.figure(figsize=(10, 5))

# Plot x vs. time
plt.subplot(1, 2, 1)
plt.plot(t, x, label="x(t)")
plt.title("Van der Pol Oscillator")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

# Phase portrait (x vs. dx/dt)
plt.subplot(1, 2, 2)
plt.plot(x, dxdt, label="Phase Space")
plt.title("Phase Portrait")
plt.xlabel("x(t)")
plt.ylabel("dx/dt")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
