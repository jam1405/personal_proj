from __future__ import annotations
import params
from typing import List
import random
from math import pi, cos, sin, atan2, sqrt
__author__ = 'Jamie Farquharson'

def forcfunc(d:float, a:float, c1:bool, c2:bool, m, cutoff_dist: float) -> float:
    
    #No force is far enough away
    if d > cutoff_dist:
        return 0,0
    
    #No force if same particle
    elif(d == 0):
        return 0, 0
    
    else: 
        #Calculate Strength of force
        f = params.STRENGTH/(d**2)
        ax = f*cos(a)/m
        ay = f*sin(a)/m
        
        #Check if particles repel or attract
        if c1 != c2:
            return -ax, -ay
        elif c1 == c2: 
            return ax, ay 
    
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
        return ang_temp

class Point:
    #General Point in 2D Grid
    x: float
    y: float
    
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    def add(self, other: Point)-> Point:
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x,y)

class Particle:
    c: int
    m: int
    location: Point
    vel: Point
    
    def __init__(self, loc:Point, vel: Point, m:int) -> None:
        loc: Point
        vel: Point
        self.m = m
        self.c = bool(random.getrandbits(1))
        self.loc = loc
        self.vel = vel
        
          
    def interact(self, other: Particle, cutoff_dist:float):
        x_diff = self.loc.x - other.loc.x
        y_diff = self.loc.y - other.loc.y
        disp = sqrt(abs(x_diff)**2 + abs(y_diff)**2)
        if disp < 0.9*params.PARTICLE_RADIUS:
            ax = params.REPULSION_STRENGTH*x_diff/params.MASS
            ay = params.REPULSION_STRENGTH*y_diff/params.MASS
            return ax, ay 
        else:
            cut = cutoff_dist
            otherc = other.c
            selfc = self.c
            ang = anglefunc(x_diff, y_diff)
        
            ax, ay = forcfunc(d=disp, a =ang, c1=selfc, c2=otherc, m=self.m, cutoff_dist=cut)
            return ax, ay
    
    def tick(self, population,num_part):
        #Reset Accelerations to 0
        ax_tot: float = 0
        ay_tot: float = 0
        
        #Sum acceleration from each other particle
        for i in range(0,num_part):
            sing_ax, sing_ay= self.interact(population[i], params.CUTOFF_DIST) 
            
            ax_tot += sing_ax
            ay_tot += sing_ay
        
        #Change location based on current velocity with change in acceleration over our TIME_STEP param
        self.vel.x = self.vel.x + ax_tot*params.TIME_STEP
        self.vel.y = self.vel.y + ay_tot*params.TIME_STEP
        self.loc.x = self.loc.x + self.vel.x*params.TIME_STEP
        self.loc.y = self.loc.y + self.vel.y*params.TIME_STEP
        
    #Colour depending on Charge
    def color(self) -> str:
        if(self.c):
            return "red"
        else:
            return "blue"
        
class Simulation:
    
    population: List[Particle]
    time: int = 0
    
    #Initialize Population with random locations and velocities
    def __init__(self, particles: int) -> None:
        self.population = []
        for _ in range(0, particles):
            init_loc = Point((random.random()-0.5)*params.BOUNDS_WIDTH, (random.random()-0.5)*params.BOUNDS_HEIGHT)
            init_vel = Point((random.random()-0.5)*params.MAX_SPEED,(random.random()-0.5)*params.MAX_SPEED)
            temp: Particle = Particle(init_loc, init_vel, params.MASS)
            self.population.append(temp)
        
    #ADVANCE TIME, cause tick update for each particle
    def tick(self):
        self.time += 1
        for particle in self.population:
            particle.tick(self.population, params.PARTICLE_COUNT)
            self.boundary_lim(particle)
        
    
    #Bounces off boundaries
    def boundary_lim(self, particle: Particle):
        #Check X Bounds
        if(particle.loc.x > params.MAX_X):
            particle.loc.x = params.MAX_X
            particle.vel.x = -particle.vel.x
        elif(particle.loc.x < -params.MAX_X):
            particle.loc.x = -params.MAX_X
            particle.vel.x = -particle.vel.x
        
        #Check Y Bounds
        if(particle.loc.y > params.MAX_Y):
            particle.loc.y = params.MAX_Y
            particle.vel.y = -particle.vel.y
        elif( particle.loc.y < -params.MAX_Y):
            particle.loc.y = -params.MAX_Y
            particle.vel.y = -particle.vel.y
        return

    
    def is_complete(self) -> bool:
        if(self.time > params.SIM_TIME):
            return True
        else: 
            return False
        
        