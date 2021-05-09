import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

legendre_ell = 2
legendre_em = 1
number_of_points = 1000

thetas = np.linspace(0., 2*np.pi, num=number_of_points)
x_values = np.cos(thetas)
radii = np.abs(sp.lpmv(legendre_em, legendre_ell, x_values))

x_values = np.multiply(x_values, radii)
y_values = np.multiply(np.sin(thetas), radii)
plt.plot(x_values, y_values)
plt.text(0.5*max(x_values), 1.2*max(y_values), r'$\ell, m = $'+str(legendre_ell)+', '+str(legendre_em))
plt.xlabel(r'$P_{\ell}^{m}(\cos\,\theta)\, \cos\,\theta$')
plt.ylabel(r'$P_{\ell}^{m}(\cos\,\theta)\, \sin\,\theta$')
plt.show()

