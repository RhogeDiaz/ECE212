import matplotlib.pylab as plt
import numpy as num
Fa = int(input('Enter the Frequency of a Analog Signal = '))
A = 5
t = num.arange(0, 1, 0.001)
x = A*num.sin(2*num.pi*Fa*t)

print("Enter 5-bit pulses")
u = []
b = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
s = 0
p = 0
shift = []
for i in t:
    if i == b[0]:
        b.pop(0)
        s = int(input())
    u.append(s)

plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Analog signal')
plt.grid(True)
plt.show()

plt.plot(t, u)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Digital Pulses')
plt.grid(True)
plt.show()
