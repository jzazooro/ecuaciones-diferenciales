from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

def ecuacioncuatro():

    t=sympy.Symbol('t')
    y=sympy.Function('y')

    f=(3*t)/2+y(t)/2*t

    sympy.Eq(y(t).diff(t), f)

    soluciongeneral=sympy.dsolve(y(t).diff(t)-f)
    
    print("la solucion general de la ecuacion es: ")
    sympy.pprint(soluciongeneral)