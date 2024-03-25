
from math import pi, atan2, sin, cos, sqrt

def forcfunc(d:float, a:float, c1:bool, c2:bool, m, cutoff_dist: float) -> float:
    
    #No force is far enough away
    if d > cutoff_dist:
        return 0,0
    
    #No force if same particle
    elif(d == 0):
        return 0, 0
    
    else: 
        #Calculate Strength of force
        f = 9000/(d**2)
        ax = f*cos(a)/m
        ay = f*sin(a)/m
        
        #Check if particles repel or attract
        if c1 != c2:
            return ax, ay
        elif c1 == c2: 
            return -ax, -ay 
    
def anglefunc(x,y)-> float: #Finds angle between points based on x-diff and y-diff
    if(x == 0 and y >=0):
        return pi/2
    elif( x==0 and y < 0):
        return 3*pi/2
    else:
        ang_temp = atan2(y,x)
       # if ang_temp < 0:
        #    ang_fin = 2*pi - ang_temp
        #else:
         #   ang_fin = ang_temp
        print(ang_temp)
        return ang_temp
    
print(forcfunc(sqrt(73),anglefunc(8,3),False,True,1,100))