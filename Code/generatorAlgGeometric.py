# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:44:07 2016

@author: Marco
"""

#ListT to matrix T^(listT[-1]) S T^(listT[-2]) ... ST^(listT[1])
def algorithmSTSingle(x,y):
    listT = []
    while(not ( not inUnitCircle(x,y) and inXlim(x))):
        listT.append(0)
        while(np.abs(x) > 0.5):
            if(x<0):
                listT[-1] +=1
                x , y = T(x,y,1)
            else:
                listT[-1] -=1
                x, y= T(x,y,-1)
    # Invert circle
        if(inUnitCircle(x,y)):
            x, y = S(x,y)
    return x,y , listT[::-1]

#plotPoints(points, "Initial Postions")
#
#for i in range(2):
#    points = algorithmST(points)
 
       
'''
Find representation in terms of S,T by using algorithmST, not sure but I think
round off errors might make this unusable at times,
g is a matrix in sltz
'''
def decomposeST(g):
    x = 0
    y = 2
    gx, gy = transform(g,x,y)
    return algorithmSTSingle(gx,gy)
def transform(g,x,y):
    a, b, c, d = g.a, g.b, g.c, g.d
    denominator = (c*x+d)**2 + (c*y)**2    
    gx = (a*c*(x**2 + y**2) + x*(a*d +b*c) +b*d)*1/denominator
    gy = y/denominator
    return gx, gy
#M = sl2z.Matrix(13,37,7,20)
M = Matrix(60,83,13,18)
Tm= Matrix(1,1,0,1) 
Sm = Matrix(0,-1,1,0)

def constructMatrix(listT):
    mat = sl2z.eye
    for power in listT:
        mat = mat @Tm**(power)@Sm
    mat = mat  @Sm**(3)
    return mat
        
x,y , listT = decomposeST(M)
print(x,y,listT)
gamma = constructMatrix(listT)    
print((gamma.inv()).entries())