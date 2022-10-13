from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

x=sympy.Symbol('x')
y=sympy.Function('y')

f=y(x)*ln(y(x))*asin(x)

sympy.Eq(y(x).diff(x), f)

solucion= sympy.dsolve(y(x).diff(x)-f)
sympy.pprint(solucion)