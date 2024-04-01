from __future__ import annotations
import params
import numpy as np

#3D Vector Class outputting a numpy 3x1 array
class Vec3():
    def __init__(self, x:float , y:float, z:float) -> None:
        self.x = x
        self.y = y
        self.z = z
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
        newx = self.x + other.x
        newy = self.y + other.y
        newz = self.z + other.z
        
        newvec = Vec3(newx,newy,newz)
        return newvec
    
    #Angle from point self --> point other
    def angle_between(self, other: Vec3)-> Vec3:
        vec = (self.vec3 - other.vec3)
        mag = np.ones(3)*np.linalg.norm(vec)
        ang = np.divide(vec, mag)
        return ang  
    
    def scal_mult(scal:float,vec:Vec3):
        newx = scal*vec.x
        newy = scal*vec.y
        newz = scal*vec.z
        newvec = Vec3(newx,newy,newz)
        return newvec
    
    
class Body():
    
    #initalize mass, radius, positions and velocity
    def __init__(self, name: str, mass:float, radius:float, pos : Vec3 , vel :Vec3) -> None:
        self.name = name
        self.m = mass
        self.r = radius #PLANET RADIUS WILL HAVE TO BE DRASTICALLY HIGHER THAN REALITY TO BE VISIBLE
        self.pos = pos
        self.vel = vel

    #Gravitational interactions with other planets
    def interact(self, bodies: list[Body]) -> Vec3:
        grav_force_tot:Vec3 = Vec3(0,0,0)
        
        #interact self with all other bodies in list
        for body in bodies:
           #If same body, return a force of 0
            if body.name == self.name:
                grav_force_tot.add(Vec3(0,0,0))
            else:
                #grav_accel = G*m/r^2
                grav_force_mag_temp: float = params.cos_const*body.m/(Vec3.dist(self.pos, body.pos)**2)
                grav_force_dir_temp: Vec3 = Vec3.angle_between(self.pos,body.pos)
                grav_force_vec_temp: Vec3 = Vec3.scal_mult(grav_force_mag_temp,grav_force_dir_temp)
                grav_force_tot.add(grav_force_vec_temp)
        
        #update new velocity and then update position
        self.vel = Vec3.add(self.vel, grav_force_tot)
        self.pos = Vec3.add(self.pos, Vec3.scal_mult(params.time_step,self.vel))
    
class Simulation:
    
    #Initializing celestial body datasets. Position will be stored as Vec3. Names , masses and radii in lists
    body_name: list =[]
    body_mass: list = []
    body_radius: list = []
    
    #Initialize time
    time: float = 0
    
    #The Planets list is grouped at first index being different planets, and second index being: 0-name, 1->mass, 2->radius, 3,4,5 -> x,y,z locations, 6,7,8 -> init vel
    def __init__(self, bodies: list) -> None:
        self.time: int = 0
        self.bodies: list[Body] = []
        self.finished = False
        for i in range(0,len(bodies)):
            self.bodies.append(Body(bodies[i,0],bodies[i,1],bodies[i,2],Vec3(bodies[i,3],bodies[i,4],bodies[i,5]),Vec3(bodies[i,6],bodies[i,7],bodies[i,8])))
    
    #Each planet updating 
    def tick(self) -> None:
        self.time += 1
        if self.time >= params.simtime:
            self.finished = True
        
        if self.finished:
            #STOP SIMULATION
            abc =1
            
        else:
            #call a body to interact with all others
            for body in self.bodies:
                body.interact(self.bodies)