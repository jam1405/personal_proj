from __future__ import annotations
import params
import numpy as np

#3D Vector Class outputting a numpy 3x1 array
class Vec3():
    def __init__(self, x:float , y:float, z:float) -> None:
        self.vec3 = np.array([x,y,z], dtype= float)
        return
    
    #Find displacement (3d vec) between 3D vectors -- for finding displacement between planets
    def disp(self, other: Vec3):
        diff = self.vec3 - other.vec3
        return diff
    
    #Find distance (scalar) betwen 2 3D vectors
    def dist(self, other: Vec3) -> float:
        return np.linalg.norm(self.vec3-other.vec3)        
    
    #Combine two 3D vectors -- for changing velocity
    def add(self, other: Vec3):
        new = self.vec3 + other.vec3
        return new
    
    #Angle from point self --> point other
    def angle_between(self, other: Vec3)-> Vec3:
        vec = (self.vec3 - other.vec3)
        mag = np.ones(3)*np.linalg.norm(vec)
        ang = np.divide(vec, mag)
        return ang  
    
class Body():
    
    #initalize mass, radius, positions and velocity
    def __init__(self, mass:float, radius:float, pos : Vec3 , vel :Vec3) -> None:
        self.m = mass
        self.r = radius #PLANET RADIUS WILL HAVE TO BE DRASTICALLY HIGHER THAN REALITY TO BE VISIBLE
        self.pos = pos
        self.vel = vel

    #Gravitational interactions with other planets
    def interact(self, other: Body) -> Vec3:
        grav_force_mag: float = params.cos_const*self.m*other.m/(Vec3.dist(self.pos, other.pos)**2)
        grav_force_dir: Vec3 = Vec3.angle_between(self.pos,other.pos)
        grav_force_vec: Vec3 = grav_force_mag*grav_force_dir
        
        #mass factor removed from grav force to indicated acceleration
        return grav_force_vec
    
    def tick(self):
        #TODO
        
        self.pos = Vec3.add(self.pos, params.time_step*Body.interact())
class Simulation:
    
    #Initializing celestial body datasets. Position will be stored as Vec3. Names , masses and radii in lists
    body_pos: Vec3
    body_name: list =[]
    body_mass: list = []
    body_radius: list = []
    
    #Initialize time
    time: float = 0
    
    #The Planets list is grouped at first index being different planets, and second index being: 0-name, 1->mass, 2->radius, 3,4,5 -> x,y,z locations
    def __init__(self, bodies: list) -> None:
        self.time: int = 0
        self.vectors: list[Vec3] = []
        
        for i in range(0,len(bodies)):
            self.body_name.append(bodies[i,0])
            self.body_mass.append(bodies[i,1])
            self.body_radius.append(bodies[i,2])
            body_pos = Vec3(bodies[i,3], bodies[i,4], bodies[i,5])
            self.vectors.append(body_pos)
    
    def tick(self) -> None:
        self.time += 1
        for Body in self.vectors:
            