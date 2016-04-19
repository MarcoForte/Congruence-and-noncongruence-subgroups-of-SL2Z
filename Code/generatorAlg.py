# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:16:20 2016

@author: Marco Forte
"""

import math
from fractions import Fraction
import sl2z
from sl2z import Matrix

#A = Matrix(23,-101,64,-281)
A = Matrix(1,0,2,1)

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

expan = splitAlg(Fraction(A.a, A.c))
prod = multAlg(expan)
inv = prod.inv()
M = inv@A

expan.append(M.b)
print(expan)