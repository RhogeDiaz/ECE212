import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 100)
def f3(x):
    # trig function: sin(x)cos(x)
    return np.sin(x) * np.cos(x)

a = 0
b = np.pi

# Analytical integral
integ_val = integrate.quad(f3, a, b)
print(integ_val)

plt.plot(x, f3(x))
plt.fill_between(x, f3(x), where =[(x > a) and (x < b) for x in x], color='green', alpha=0.5, label=str(integ_val))
plt.legend()
plt.title("Analytical Integration")
plt.show()

# Integral approximation function
def integral_approximation(f, a, b):
    return (b - a) * np.mean(f)

x_range = np.arange(a, b + 0.0001, .0001)
fx = f3(x_range)
# Approximate integral
approx = integral_approximation(fx, a, b)
print(approx)
plt.plot(x_range, fx, 'o-')
plt.fill_between(x_range, fx, where =[(x_range > a) and (x_range < b) for x_range in x_range], color='green', alpha=0.5, label=str(approx))
plt.legend()
plt.title("Numerical Integration")
plt.show()
