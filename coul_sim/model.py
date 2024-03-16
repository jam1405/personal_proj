from __future__ import annotations
from coul_sim import params
import numpy as np
from typing import List
import random

__author__ = 'Jamie Farquharson'

def forcfunc(d:float, a:float, c1:int, c2:int, m, cutoff_dist: float) --> float:
    if d > cutoff_dist:
        return 0,0
    else: 
        f = c1*c2/(d^2)
        fx = f*np.cos(a)/m
        fy = f*np.sin(a)/m
        return fx, fy
    
def anglefunc(x,y)-> float: #Finds angle between points based on x-diff and y-diff
    ang_temp = np.arctan2(y/x)
    if ang_temp < 0:
        ang_fin = 2*np.pi - ang_temp
    else:
        ang_fin = ang_temp
    return ang_fin

class Point:
    #General Point in 2D Grid
    x: float
    y: float
    
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    def disp(self, other: Point):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        disp: float = np.sqrt(abs(x_diff)**2 + abs(y_diff)**2)
        ang: float = anglefunc(x_diff, y_diff)
        return disp, ang
    
    def add(self, other: Point):
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x,y)

class Particle:
    c: int
    m: int
    location: Point
    vel: Point
    
    def __init__(self, m:int, c:int) -> None:
        location: Point
        vel: Point
        self.m = m
        self.c = c 
        self.loc = location
        self.vel = vel
          
    def interact(self, other: Particle, cutoff_dist):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        disp = np.sqrt(abs(x_diff)**2 + abs(y_diff)**2)
        ang = anglefunc(x_diff, y_diff)
        fx, fy = forcfunc(disp, ang, self.c, other.c, cutoff_dist)
        return fx, fy
    
    #Colour depending on Charge
    def color(self) -> str:
        if self.c > 0:
            return "red"
        else:
            return "blue"
        
class Simulation:
    
    population: List[Particle]
    time: int = 0
    
    def __init__(self, particles: int, speed:float) -> None:
        self.population = []
        
    #ADVANCE TIME
    def tick(self):
        self.time += 1
        
    #RANDOM START LOCATION
    def random_loc(self) -> Point:
        x = random.random() * params.BOUNDS_WIDTH
        y = random.random() * params.BOUNDS_HEIGHT
        
        return Point(x, y)
    
    #RANDOM START VELOCITY
    def random_vel(self) -> Point:
        x_vel = random.random() * params.MAX_SPEED
        y_vel = random.random() * params.MAX_SPEED
        return Point(x_vel, y_vel)
    
    #Bounces off boundaries
    def boundary_lim(self, particle: Particle):
        
        return
    
    def is_complete(self) -> bool:
        if self.time > params.SIM_TIME:
            return True
        else: 
            return False
        
        