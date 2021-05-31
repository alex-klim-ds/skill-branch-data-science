import numpy as np

"""1: посчитать значение производной функции
#$\cos(x) + 0.05x^3 + \log_2{x^2}$ в точке $x = 10$."""
def function_1(x):
    return np.cos(x) + 0.05 * x**3 + \
        np.log2(x**2)
def derivation(x):#производная от function_1(x)
    return - np.sin(x) + 0.15 * x**2 + \
           (2 / (x * np.log(2)))
print('1: Значение производной' +' '+ str(round(derivation(10), 2)))

"""2: посчитать значение градиента функции
$x_1^2\cos(x_2) + 0.05x_2^3 + 3x_1^3"""
def function_2(x1, x2):
    return x1**2 * np.cos(x2) + 0.05 * x2**3 + \
           3 * x1**3 * np.log2(x2**2)
def d_dx1(x1, x2):#частная производная по x1
    return 9*x1**2 * np.log2(x2**2) + \
                 2 * x1 * np.cos(x2)
def d_dx2(x1, x2):#частная производная по x2
    return round(0.15 * x1**2 +\
                 ((6 * x1**3) / np.log(2) * (x2)) - \
                 x1**2 * np.sin(x2), 2)
def gradient(x1, x2):
    return ([d_dx1(x1, x2), d_dx2(x1, x2)])

print('2: Градиент функции:' +' '+ str(round(gradient(10, 1), 2)))
