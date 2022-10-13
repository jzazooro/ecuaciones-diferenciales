# ecuaciones-diferenciales

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/ecuaciones-diferenciales.git)

He creado un programa que resuelve cuaro ecuaciones diferenciales de primer orden, dos de ellas con una condicion inicial. Para ello ha sido muy util la biblioteca sympy.

El codigo que he creado es el siguiente:

### main

```
from lanzador import main

if __name__ == "__main__":
    main()
```

### lanzador

```
from ecuaciones.ecuacion1 import ecuacionuno
from ecuaciones.ecuacion2 import ecuaciondos
from ecuaciones.ecuacion3 import ecuaciontres
from ecuaciones.ecuacion4 import ecuacioncuatro

def main():
    ecuacionuno()
    ecuaciondos()
    ecuaciontres()
    ecuacioncuatro()
```

### ecuacion1

```
from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

def ecuacionuno():

    x=sympy.Symbol('x')
    y=sympy.Function('y')

    f=((x**2)*y(x)-y(x))/(y(x)-1)

    sympy.Eq(y(x).diff(x), f)

    condicion={y(3): -1}

    soluciongeneral=sympy.dsolve(y(x).diff(x)-f)
    solucionfinal= sympy.dsolve(y(x).diff(x)-f, ics=condicion)

    print("la solucion general de la ecuacion es: ")
    sympy.pprint(soluciongeneral)

    print("la solucion con la condicion inicial de la ecuacion es: ")
    sympy.pprint(solucionfinal)
```

### ecuacion2

```
from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

def ecuaciondos():

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
```
### ecuacion3

```
from sympy import*
import sympy
import math
import numpy as np
import matplotlib as plt

def ecuaciontres():

    t=sympy.Symbol('t')
    y=sympy.Function('y')

    f=2*(2-t)**2+(y(t))/(t-2)

    sympy.Eq(y(t).diff(t), f)

    soluciongeneral=sympy.dsolve(y(t).diff(t)-f)

    print("la solucion general de la ecuacion es: ")
    sympy.pprint(soluciongeneral)
```

### ecuacion4

```
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
```
