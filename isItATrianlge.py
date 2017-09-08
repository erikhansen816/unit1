#Erik Hansen
#9/7/2017
#isItATriangle.py

sidea = float(input('Enter side A: '))
sideb = float(input('Enter side B: '))
sidec = float(input('Enter side C: '))

smallside = min(sidea,sideb,sidec)
bigside = max(sidea,sideb,sidec)
middleside = sidea+sideb+sidec-(smallside+bigside)
print(middleside+smallside>bigside)

