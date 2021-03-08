"""
    This file contains commonly used functions between the files in this repository.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def wag_the_dog(potential, x_range=(0,5), k_values=np.linspace(0.9, 1.1, 10), initial_values=(1.,0.)):
    """
        This function numerically solves the wave equation for a harmonic oscillator, based on a 'guess' for k and goes from there. This is for the problem 2.55 in Griffth's quantum mechanics (3rd edition).
    """
    positions = np.linspace(x_range[0], x_range[1], 1000)

    allowed_potentials = ['harmonic oscillator']
    if potential == allowed_potentials[0]:
      print("Assuming harmonic oscillator...")
      for k_value in k_values:  
        # Differential equation
        psi_prime = lambda xi, psi, k: [psi[1], (xi**2-k)*psi[0]]

        # Solve differential equation using scipy
        sol = solve_ivp(psi_prime, x_range, initial_values, t_eval=positions, args=[k_value])

        # Plot solution
        plt.plot(positions, sol.y[0], label=fr'$k^2$: {k_value:.4f}')

    # Plotting configuration
    plt.legend()
    plt.axhline(c='black')
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\psi_n(\xi)$')
    plt.ylim(-3,3)
    plt.show()
  