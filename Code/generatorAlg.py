# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:16:20 2016

@author: Marco Forte
"""

import math
from fractions import Fraction
from sl2z import Matrix

mat = Matrix(23,-101,64,-281)

T = Matrix(1,1,0,1) 
S = Matrix(0,-1,1,0)

def splitAlg(frac):
        ceilFrac = math.ceil(frac)
        if frac.denominator!=1:
          return [ceilFrac] + splitAlg( 1/(ceilFrac - frac))
        else:
            return [ceilFrac]
            
def multAlg(expan):
    prod = sl2z.eye
    for power in expan:
        prod = prod@T**(power)@S
    return prod

expan = splitAlg(Fraction(mat.a, mat.c))
prod = multAlg(expan)
inv = prod.inv()
M = inv@mat

expan.append(M.b)
print(expan)
    