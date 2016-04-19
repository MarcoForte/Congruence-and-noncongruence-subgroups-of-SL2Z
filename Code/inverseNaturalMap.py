# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:48:33 2016
Given  A,N, where A is in sl2(z/N)
Return B in Sl2z such that B congruent to A mod N
@author: Marco
"""

#import math
#from fractions import Fraction
from sl2z import Matrix

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        
N = 3
A = Matrix(8,47,30,8)

a, b, c, d = A.a, A.b, A.c, A.d 
k = 1
b1 = b
gcd, x, y = egcd(a,b1)
while(gcd !=1):
    b1 = b1+k*N
    gcd, x, y = egcd(a,b1)
    k+=1

relPrimeA = Matrix(a,b1,c,d)
c1 = c -y*(1 - relPrimeA.det())
d1 = d + x*(1- relPrimeA.det())
print(a,b1,c1,d1)