import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def model(z, t):
    dxdt = z[1]
    dydt = -2 * z[1] - 2 * z[0]
    dzdt = [dxdt, dydt]
    return dzdt

# initial condition
z0 = [0, 1]

# time points
t = np.linspace(0, 10)

# solve ODE
z = odeint(model, z0, t)

# plot results
plt.plot(t, z[:, 0], 'b-', label=r'$\frac{dx}{dt}=y$')
plt.plot(t, z[:, 1], 'r--', label=r'$\frac{dy}{dt}=-2y - 2x$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
