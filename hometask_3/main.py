from sympy import *
import numpy as np
import math
#import matplotlib.pyplot as plt
x = 10
a = (diff(cos(x)+0.05*x**3))
b = math.log2(x)**2
print(a + b)
#plt.plot (a, b)
#plt.show()