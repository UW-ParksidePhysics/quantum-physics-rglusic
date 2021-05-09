#!/usr/bin/env python
# coding: utf-8

# # Approximating the Probability Density for a Harmonic Oscillator
# As per the problem, we need 1.11(b) solution to begin.
# 
# $\rho(x)=\frac{1}{\pi\sqrt{a^2-x^2}}$, where $a$ is our upper bound.
# 
# Integrating this, one can verify that it is indeed normalized and equal to one from some $-a$ to $a$.
# 
# This is our analytical solution, now our numerical solution is as follows:
# 
# $\rho_{approx}(x)=$a$\cdot\cos(\omega t)$, where we let a and $\omega$ both equal $1$ as stated in the problem.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 5
w = 1

# Point generation
x_inputs = np.linspace(-a, a, 10000)
analytical = 1/(np.pi*np.sqrt(a**2-x_inputs**2))
approx = a*np.cos(w*x_inputs)


# # Visualization of the Probability Density
# Below we can use the results from above to visual our approximation. Using a histogram is the easiest way

# In[10]:


times = np.pi * np.random.rand(10000)
cosine = np.cos(times)
plt.hist(cosine, label='Probability Approx')
plt.plot(np.linspace(-1, 1, 10000), 2000/(np.pi*np.sqrt(1**2 - np.linspace(-1, 1, 10000)**2)), label=r"$\rho(x)$")
plt.ylim(0, 2000)
plt.title(r"Monte-Carlo PDF Along with Exact PDF ($\rho(x)$)")
plt.ylabel(r"$\rho(x)$")
plt.xlabel(r"$x$")
plt.legend()
plt.show()

