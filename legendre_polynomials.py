import numpy as np
from scipy.special import eval_legendre
import matplotlib.pyplot as plt

maximum_n = 4
x_values = np.linspace(-1, 1)
for n in range(maximum_n+1):
    y_values = eval_legendre(n, x_values)
    plt.plot(x_values, y_values, label=r'$n =$ '+str(n))

plt.xlabel(r'$x$')
plt.ylabel(r'$P_n(x)$')
plt.axhline(color='black')
plt.axvline(color='black')
plt.legend()
plt.show()
