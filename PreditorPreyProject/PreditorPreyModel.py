#!/usr/bin/env python

"""
author: Theo Koppenhöfer

"""

# imports
import sympy as sp
from sympy import simplify, symbols, Rational
from sympy.matrices import Matrix

# define symbols
x, y = sp.symbols('x y') # stands for R, F
r_R, K_R, alpha, B, b_F = symbols('r_R K_R alpha B b_F')

# define f
f = [r_R*x*(1-x/K_R-alpha*y),x*y/B-b_F*y]

# differentiate
Df = Matrix([[simplify(sp.diff(f[i], j)) for j in [x,y]] for i in [0,1]])

evalslist = [] # list of eigenvalues of Df
equilibria = [[0,0],[K_R,0],[B*b_F,(1-B*b_F)/alpha]] # list of equilibrium points
for x0,y0 in equilibria:
    print(f'x={x0}, y={y0}')
    Df_x0 = Df.subs([(x,x0),(y,y0),(alpha,Rational('1/10')),(b_F,Rational('1/5')),(B,1000),(r_R,2)]) # evaluate the derivative at x0,y0
    print('derivative Df_x0=',Df_x0)
    evalslist += [simplify(Matrix(list(Df_x0.eigenvals().keys())))]
    print('eigenvalues :',evalslist[-1])
    print()
