#Erik Hansen
#9/6/2017
#programSlope.py - finding slope and equation of line

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
slope = (y2-y1)/(x2-x1)
print('The slope is',slope)
b = y1-(slope*x1)
print('The equation of the line is Y =',slope,'X +',b)