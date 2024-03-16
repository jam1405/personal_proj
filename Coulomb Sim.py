import numpy as np
import matplotlib.pyplot as plt
import simpy as sim

#Initialize environment
env = sim.Environment()

#Sim Variables
dim_of_box = 30
num_part = 10
dt = 0.1
cutoff_dist = 10
m=1



#Set up distance (Nx2), angle, force arrays (NxN), and charge (Nx1)
dist_initial = np.random.random((num_part,2))
dist = dim_of_box*dist_initial
char = np.array((num_part,1))
vel_arr = np.array((num_part, 2))
ang = np.array(num_part,num_part)
forc = np.array(num_part,num_part)


#Useful functions
def anglefunc(x,y): #Finds angle between points based on x-diff and y-diff
    ang_temp = np.arctan2(y/x)
    if ang_temp < 0:
        ang_fin = 2*np.pi - ang_temp
    else:
        ang_fin = ang_temp
    return ang_fin

def forcfunc(d, a, c1, c2):
    if d > cutoff_dist:
        return 0,0
    else: 
        f = c1*c2/(d^2)
        fx = f*np.cos(a)
        fy = f*np.sin(a)
        return fx, fy
            
#Loop through each particle
for i in range(num_part):
    
    #loop through each other particle
    for j in range(num_part):
        
        #Distance Between particles and angle
        dispx = dist[i,0] - dist[j,0]
        dispy = dist[i,1] - dist[j,1]
        disp = np.sqrt(dispx^2 + dispy^2)
        ang[i,j] = anglefunc(dispx,dispy)
        
        #Magnitude of force between
        forc[i,j] = forcfunc(disp, ang[i,j], char[i],char[j])
        accel = forc[i,j]/m
        vel_arr[i,0] = vel_arr[i,0] + accel*dt

class Particle:
    
    def __init__(self,charge,mass, posx, posy,env) -> None:
        self.chg = charge
        self.m = mass
        position = np.array((2,1))
        position[0] = posx
        position[1] = posy
        self.pos = position
        self.env = env 
        pass