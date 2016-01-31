# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:17:38 2016

@author: Marco
"""
# Class for sl2z matrices
class Matrix:
    def __init__(self, a, b,c,d):
         self.a = a
         self.b = b
         self.c = c
         self.d = d
    def det(self):
        return self.a * self.d - self.b*self.c
    def inv(self):
        return Matrix(self.d,-self.b,-self.c,self.a)
    def __matmul__(self,other):
        return Matrix(self.a*other.a + self.b*other.c, self.a*other.b + self.b*other.d,
                      self.c*other.a + self.d*other.c ,self.c*other.b + self.d*other.d)
    def __pow__(self,n):
        prod = eye
        for i in range(n):
            prod@=self
        return prod

eye = Matrix(1,0,0,1)