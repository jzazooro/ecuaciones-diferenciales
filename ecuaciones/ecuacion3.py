from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

t=sympy.Symbol('t')
y=sympy.Function('y')

f=2*(2-t)**2+(y(t))/(t-2)

sympy.Eq(y(t).diff(t), f)

solucion=sympy.dsolve(y(t).diff(t)-f)
sympy.pprint(solucion)