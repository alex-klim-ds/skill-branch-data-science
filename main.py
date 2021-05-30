import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
def function_1(x):
    return round(np.cos(x) + 0.05 * x**3 + \
        np.log2(x**2), 2)
def function_2(x1, x2):
    return round(x1**2 * np.cos(x2) + 0.05 * x2**3 + \
           3 * x1**3 * np.log2(x2**2), 2)

"""1: посчитать значение производной функции
#$\cos(x) + 0.05x^3 + \log_2{x^2}$ в точке $x = 10$."""
def derivation(x):#производная от function_1(x)
    return - np.sin(x) + 0.15 * x**2 + \
           (2 / (x * np.log(2)))
print('1: Значение производной' +' '+ str(round(derivation(10), 2)))

"""2: посчитать значение градиента функции
$x_1^2\cos(x_2) + 0.05x_2^3 + 3x_1^3"""
def d_dx1(x1, x2):#частная производная по x1
    return round(9*x1**2 * np.log2(x2**2) + \
                 2 * x1 * np.cos(x2), 2)
def d_dx2(x1, x2):#частная производная по x2
    return round(0.15 * x1**2 +\
                 ((6 * x1**3) / np.log(2) * (x2)) - \
                 x1**2 * np.sin(x2), 2)
def gradient(x1, x2):
    return ([d_dx1(x1, x2), d_dx2(x1, x2)])

print('2: Градиент функции:' +' '+ str(gradient(10, 1)))

"""3: найти точку минимума для функции
$\cos(x) + 0.05x^3 + \log_2{x^2}$.
Зафиксировать параметр $\epsilon = 0.001$,
начальное значение принять равным 10."""
print('3:')
def function_1(x):
    return np.cos(x) + 0.05 * (x)**3 + np.log2(x**2)
x = np.arange(-2.0, 10.0, 0.01)
y = function_1(x)
plt.plot(x, y,'b')
step = 0.1 # шаг спуска
xn = 10
yn = function_1(xn)
Y = {xn: yn}
for _ in range(50): # 50 максимальное число итераций по условию
    xn = xn - step*misc.derivative(function_1, xn)
    yn = function_1(xn)
    Y[xn] = yn
    # выводим результат каждой итерации
    print("x=", format(xn, ".2f"), "; " "y=", format(yn, ".2f"))
plt.title("Gradient optimization one dim")
plt.plot(list(Y.keys()), list(Y.values()), 'ro')
plt.show()

X = {}
for i in range(len(Y)):
    X[list(Y.values())[i]] = list(Y.keys())[i]
plt.plot(list(Y.keys()), list(Y.values()))

# выводим пару искомых минимальных X и Y (близких к минимумам)
print ('мин. функции в т. Х =', min(X.items())[1])
print ('мин. функции в т. Y =', min(X.items())[0])
