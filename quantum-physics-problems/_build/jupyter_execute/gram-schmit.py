#!/usr/bin/env python
# coding: utf-8

# # Gram-Schmidt Orthonormalization
# The following produces the Gram-Schmit orthonormalization on arbitrary basis vectors. In the case of this example, we will be using the following vectors:
# 
# $|𝑒1⟩=(1+𝑖)𝑖̂+(1)𝑗̂+(𝑖)𝑘̂$, $|𝑒2⟩=(𝑖)𝑖̂+(3)𝑗̂+(1)𝑘̂$, $|𝑒3⟩=(0)𝑖̂+(28)𝑗̂+(8)𝑘̂$

# # The Gram-Schmidt
# We can create our Gram-Schmit Orthonormalization function:

# In[1]:


import numpy as np
def gram_schmidt(vectors):
    bases = []
    for vec in vectors:
        w = vec - np.sum(np.dot(vec, q) * q for q in bases)
        bases.append(w / np.linalg.norm(w))
    return np.array(bases)


# # Example Bases
# Let's now use our `gram_schmidt` function to evaluate the original bases given at the top of this page:
# 
# $|𝑒1⟩=(1+𝑖)𝑖̂+(1)𝑗̂+(𝑖)𝑘̂$, $|𝑒2⟩=(𝑖)𝑖̂+(3)𝑗̂+(1)𝑘̂$, $|𝑒3⟩=(0)𝑖̂+(28)𝑗̂+(8)𝑘̂$

# In[2]:


bases = np.array([
    [1+1.j, 1., 1.j],
    [1.j, 3., 1.],
    [0., 28., 8.]
]).T

print(gram_schmidt(bases))


# # Another Example
# Below I test the following basis vectors as required by the Homework 3B assignment:
# $ |𝑒1⟩=(1+𝑖)𝑖̂+(1)𝑗̂+(𝑖)𝑘̂, |𝑒2⟩=(𝑖)𝑖̂+(3)𝑗̂+(1)𝑘̂, |𝑒3⟩=(0)𝑖̂+(28)𝑗̂+(8)𝑘$
# 
# Note: I enter them as row vectors, then transpose them using .T as it's easier to type.

# In[3]:


bases_2 = np.array([
    [1+1.j, 1, 1.j],
    [1.j, 3, 1],
    [0, 28, 8]
]).T

print(gram_schmidt(bases_2))

