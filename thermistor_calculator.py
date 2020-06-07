import math
import numpy as np
import matplotlib.pyplot as plt

"""-----    Settings    -----"""

# Target temperature range: (lower, upper)
temp_range = [0, 100]
num_data_points = 100
beta_val = 3950
reference_temp = 25
nominal_resistance = 100000

C_TO_K = 273
plot_curve = False

"""-----    Calcs    -----"""
temp_range = [i + C_TO_K for i in temp_range]
reference_temp += C_TO_K

temps = np.linspace(temp_range[0], temp_range[1], num_data_points)

# Magic Equation
resistance = nominal_resistance * math.e ** (beta_val*((1.0/temps) - (1.0/reference_temp)))

# Convert back to Celsius
#temps -= C_TO_K

# Fitting a polynomial
degree = 7      # Degree of poly
poly = np.poly1d(np.polyfit(resistance, temps, degree))

print(poly)
print(poly(100000) - 273)

#new_resistance = -1.139e-14*temps**3 + 6.846e-09*temps**2 - 0.001332*temps + 95.63

"""
Polynomial

            15             14             13             12
-1.717e-75 x  + 4.385e-69 x  - 5.072e-63 x  + 3.515e-57 x 
              11             10             9             8
 - 1.627e-51 x  + 5.313e-46 x  - 1.259e-40 x + 2.196e-35 x
              7             6             5             4             3
 - 2.829e-30 x + 2.681e-25 x - 1.847e-20 x + 9.073e-16 x - 3.096e-11 x
              2
 + 7.132e-07 x - 0.01115 x + 424.4

"""

temps -= C_TO_K
plt.plot(resistance, temps)

plt.show()