import matplotlib.pyplot as plt
import numpy as np

age_distribution = {
      14: 1,
      15: 1,
      16: 3,
      22: 2,
      24: 2,
      25: 5,
}

# j
ages = [*age_distribution]
# N(j)
numbers = [age_distribution[age] for age in ages]

# Plot N(j) vs j
#plt.bar(ages, numbers)
#plt.ylim(0, 6)
#plt.ylabel(r'$N(j)$')
#plt.xlim(10, 27)
#plt.xlabel(r'$j$')
#plt.show()

# N
total_number = sum(age_distribution.values())
print('N = {}'.format(total_number))

# P(15)
probability_distribution = np.zeros(26)
for age in age_distribution:
  probability_distribution[age] = age_distribution[age]/total_number

print(probability_distribution)
print('P(15) = {}'.format(probability_distribution[15]))

# sum of probabilities
probability_sum = sum(probability_distribution)
print('sum(P) = {}'.format(probability_sum))

# most probable age
most_probable_age = max(age_distribution)
#most_probable_age = 
print('max(P) = {}'.format(most_probable_age))

# median age
median = total_number/2
age = 0
print('P reaches 0.5 at j={}'.format(age))

# average age
mean_age = 0.
for key in age_distribution:
  mean_age += key*age_distribution[key]
mean_age = mean_age/total_number
# or:
mean_age2 = 0.
print('<j> = {} = {}'.format(mean_age, mean_age2))

# expectation value of j^2
age_squared_expectation = 0.
for age in age_distribution:
  age_sqr = age**2
  age_squared_expectation += age_sqr * probability_distribution[age]
print('<j^2> = {}'.format(age_squared_expectation))
print('<j>^2 = {}'.format(mean_age**2))

# Δj
delta_j = 0.
for j in age_distribution:
  delta_j += j - mean_age
delta_j /= total_number
print('Δj = {}'.format(delta_j))

# <Δj>
delta_j_expectation = 0.
for j in age_distribution:
  delta_j_expectation += (j-mean_age)*probability_distribution[j]
print('<Δj> = {}'.format(delta_j_expectation))

# σ^2
probability_distribution_array = 0.
delta_jsqr_expectation = 0.
for j in age_distribution:
  delta_jsqr_expectation += (j-mean_age)**2 * probability_distribution[j]

variance = delta_jsqr_expectation
print('σ^2 = {} = {}'.format(variance, age_squared_expectation - mean_age**2))

# σ
standard_deviation = np.sqrt(variance)
print('σ = {}'.format(standard_deviation))
