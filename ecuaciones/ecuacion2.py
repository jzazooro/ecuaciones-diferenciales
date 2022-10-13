from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

x=sympy.Symbol('x')
y=sympy.Function('y')

f=y(x)*ln(y(x))*asin(x)

sympy.Eq(y(x).diff(x), f)

condicion={y((math.pi)/2): math.e}

soluciongeneral= sympy.dsolve(y(x).diff(x)-f)
solucionfinal= sympy.dsolve(y(x).diff(x)-f, ics=condicion)

print("la solucion general de la ecuacion es: ")
sympy.pprint(soluciongeneral)

print("la solucion con la condicion inicial de la ecuacion es: ")
sympy.pprint(solucionfinal)