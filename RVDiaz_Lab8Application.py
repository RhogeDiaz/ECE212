xstart = -2
xstop = 2.1
increment = 0.1
x = np.arange(xstart, xstop, increment)

fx = [1, 0, 3]
p1 = np.poly1d([fx[2], fx[1], fx[0]]) 
print("\n\nThe Given f(x) is\n",p1) 
y=(fx[2]*(x**2)+fx[1])

# Exact/Analytical Solution
dydx = poly.polyder(fx) 
p2 = np.poly1d([dydx[1], dydx[0]])
print("\n\nThe Derivative is",p2) 
dy_exact=dydx[1]*x 
plt.plot(x, dy_exact, 'o-')

# Numerical Solution
dydx_num = np.diff(y) / np.diff(x); 
print("\n\ndydx_num", dydx_num)
xstart = -2
xstop = 2
x2 = np.arange(xstart,xstop,increment)

plt.plot(x2, dydx_num, 'o-') 
plt.title("dy/dx")
plt.legend(["Exact", "Numeric"])
plt.show()