from sympy import *
import math
import numpy as np
from Office.save_file import save_to_csv
# x = symbols('x')
# print(integrate(cos(x) ,x))
# d = diff(exp(x**2), x)
# integrate(exp(-x), (x, 0, oo))
#integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# x, y, z, t = symbols('x y z t')
# jf = integrate((1-cos(x))*x, (x, 0, 18))
# print(jf)

def jifen(expression):
    x = symbols('x')
    res = integrate(expression, x)
    return res

def qiudao(expression):
    x = symbols('x')
    res = diff(expression, x)
    return res
#
# print(qiudao('e**x'))


def get_c(cost,debt):
    x = symbols('x')
    c = solve(((x - x ** 2 / 18 + (((1 - cost) * x ** 2) / 36))) / 0.05 - debt, x)
    return c

vu = 135
for cost in np.arange(0.1,1.1,0.1):
    for debt in range(10,200,10):
        c = get_c(cost=cost,debt=debt)
        li = c +[cost,debt]
        save_to_csv('gscw',li)

# cost = 0.5
# debt = 10
# c = get_c(cost,debt)
# li =

# for v in c:
#     if v >0:
#         print(v)
