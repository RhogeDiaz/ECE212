#Rhoge Vhir A. Diaz
#ECE 2A

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.integrate import quad

# function: 2e^x(sec(x))
def f(x):
    return 2 * np.exp(x) * (1 / np.cos(x))

# drivative
def df(x):
    return derivative(f, x, dx=1e-6)

# integral
def integral(x):
    return quad(f, 0, x)[0]

# user input
increment = float(input("Enter the increment value: "))

# x values
x = np.arange(0, 10, increment)

# Calculate y values for the function, its derivative, and its integral
y = f(x)
dy = df(x)
y_integral = np.array([integral(xi) for xi in x])

# plotting the function and derivative
plt.figure(figsize=(12, 8))
plt.plot(x, y, label='f(x) = 2e^x * sec(x)')
plt.plot(x, dy, label="f'(x)")
plt.legend()
plt.show()

# plotting the integral
plt.plot(x, y_integral, label='∫f(x) dx')
plt.legend()
plt.grid(True)
plt.show()
