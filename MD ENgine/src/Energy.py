import numpy as np
from sympy import symbols, diff, lambdify

k = 0.1

def pe(x):
    return 0.5*k*x*x

def ke_sys(V):
    return np.sum(V**2) * 0.5
    
def pe_sys(X):
    te = 0
    for l in X:
        te += pe(np.sqrt(np.sum((X-l)**2)))
    return te


# Force calculations from PE
x = symbols('x')
f = pe(x)
force = diff(f, x)
For = lambdify(x, force)

def F(x):
    return For(x)


