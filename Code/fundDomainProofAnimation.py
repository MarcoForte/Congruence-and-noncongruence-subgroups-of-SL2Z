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
    plt.xlim(-2,2)
    plt.ylim(0,2.1)

    
#Check if point outside unit circle
def inUnitCircle(x,y):
    return x**2 + y**2 <1
# Check if in range -0.5,0.5
def inXlim(x):
    return np.abs(x)<=0.5
    
# Draw points to consider
xPoints = np.linspace(-1.5,1.5,7)
yPoints = np.linspace(0.25,1.5,6)
points = np.transpose([np.tile(xPoints, len(yPoints)), np.repeat(yPoints, len(xPoints))])
#points = np.array([[np.pi/2,0.137], [np.pi/3,0.45],  [-np.sqrt(2)/2,0.11],  [-0.9,0.8]])
#points = np.array([[0.6,0.1],[0.6,0.2],[0.6,0.4],[0.6,0.6],[0.6,0.8],[0.6,1.0],[0.6,1.2],[0.6,1.5]])
#pointColors = ['red','black','blue','green']

# Plots points and colours
def plotPoints(points,title):
    plotOutline()
    for i, point in enumerate(points):
        x , y = point[0], point[1]
        if(inUnitCircle(x,y)):
            plt.plot(x,y,'bd',markersize= 9)
        else:
            plt.plot(x,y,'ro',markersize= 9)
    plt.title(title)
    fig = plt.gcf()
    fig.savefig(str(np.random.randint(1000))+title+".png",dpi = 1000)
    plt.show()
def T(x,y,n=1): return  x + n, y
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

#plotPoints(points,"InitialPositions")
#points = algorithmST(points)
#algorithmST(points)
plotPoints(points,"Initial Positions")
#Tpoints = [T(point[0],point[1]) for point in points]
#plotPoints(Tpoints,"After transforming by T")
Spoints = [S(point[0],point[1]) for point in points]
plotPoints(Spoints,"After transforming by S")
#plt.title("Actions of S and T on a line")
#plt.savefig("Actions of S and T on a line.png",dpi =1000)
        
        
        
        
        
        
        
        
        