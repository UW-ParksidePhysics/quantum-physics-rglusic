from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
en = 3
em = 2
x = np.real(sph_harm(em, en, theta, phi)) * np.outer(np.cos(phi), np.sin(theta))
y = np.real(sph_harm(em, en, theta, phi)) * np.outer(np.sin(phi), np.sin(theta))
z = np.real(sph_harm(em, en, theta, phi)) * np.outer(np.ones(np.size(phi)), np.cos(theta))

# Plot the surface
ax.plot_surface(x, y, z, color='b', alpha=0.1)

plt.show()
