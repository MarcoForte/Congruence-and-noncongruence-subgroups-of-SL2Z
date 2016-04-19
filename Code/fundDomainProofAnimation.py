# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:47:19 2016

@author: Marco
"""
import numpy as np
import math
from sl2z import Matrix
import matplotlib.pyplot as plt
# Plot outline of Fundamental domain
def plotOutline():
    x = np.linspace(-1, 1, 1000);
    y = np.sqrt( 1- x**2)
    ax = plt.gca()
    plt.plot(x, y)
    plt.plot((-0.5, -0.5), (np.sqrt(3)/2, 5), 'k-')
    plt.plot((0.5, 0.5), (np.sqrt(3)/2, 5), 'k-')
    plt.axhline(y=0,color = 'k')
    plt.xlim(-3.5,3)
    plt.ylim(0,3)

    
#Check if point outside unit circle
def inUnitCircle(x,y):
    return x**2 + y**2 <1
# Check if in range -0.5,0.5
def inXlim(x):
    return np.abs(x)<=0.5
    
# Draw points to consider
#xPoints = np.linspace(-1.5,1.5,7)
#yPoints = np.linspace(0.25,1.5,6)
#points = np.transpose([np.tile(xPoints, len(yPoints)), np.repeat(yPoints, len(xPoints))])
points = np.array([[np.pi/2,0.137], [np.pi/3,0.45],  [-np.sqrt(2)/2,0.11],  [-0.9,0.8]])

pointColors = ['red','black','blue','green']
# Plots points and colours
def plotPoints(points,title):
    plotOutline()
    for i, point in enumerate(points):
        x , y = point[0], point[1]
        plt.plot(x,y, 'o',color = pointColors[i])
    plt.title(title)
    fig = plt.gcf()
    fig.savefig("image"+str(np.random.randint(1000)) + title+".png")
    plt.show()
def T(x,y,n): return  x + n, y
def S(x,y):  return (-x/(x**2+y**2)),  (y/(x**2+y**2))
# Algorithm to move points
''' 
Move points into fundamental domain by Succesive action of S,T
1) Move point via T, untill -1/2<=x<=1/2, 
If in fund domain ok. plot
2) If not, use unit circle to invert, plot
3) step 1)
'''
def algorithmST(points):
    # Move T
    for point in points:
        x , y = point[0], point[1]
        while(np.abs(x) > 0.5):
            if(x<0):
                x , y = T(x,y,1)
            else:
                x, y= T(x,y,-1)
        point[0], point[1] = x, y
    plotPoints(points,"Step 1, apply T^n")
    # Invert circle
    # Move T
    for point in points:
        x , y = point[0], point[1]
        if(inUnitCircle(x,y)):
            x, y = S(x,y)
        point[0], point[1] = x, y
    plotPoints(points,"Step 2, apply S")
    return points
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

        
        
        
        
        
        
        
        
        
        
        
        