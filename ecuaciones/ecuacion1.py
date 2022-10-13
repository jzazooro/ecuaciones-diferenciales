from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

x=sympy.Symbol('x')
y=sympy.Function('y')

f=((x**2)*y(x)-y(x))/(y(x)-1)

equac=sympy.Eq(y(x).diff(x), f)

solucion= sympy.dsolve(y(x).diff(x)-f)
sympy.pprint(solucion)