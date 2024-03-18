#Test
from __future__ import annotations
import numpy as np
class Vec3():
    def __init__(self, x:float , y:float, z:float) -> None:
        self.vec3 = np.array([x,y,z], dtype= float)
        self.uvec = np.linalg.norm(self.vec3)
        return
    
    #Find difference between 3D vectors -- for finding displacement between planets
    def disp(self, other: Vec3) -> Vec3:
        diff = self.vec3 - other.vec3
        return diff
    
    #Combine two 3D vectors -- for changing velocity
    def add(self, other: Vec3) -> Vec3:
        new = self.vec3 + other.vec3
        return new
    
    def angle_between(self, other: Vec3)-> Vec3:
        vec = (self.vec3 - other.vec3)
        mag = np.ones(3)*np.linalg.norm(vec)
        ang = np.divide(vec, mag)
        return ang  
    
x= Vec3(1,0,0)
y = Vec3(0,1,0)

print(x.vec3)
print(y.vec3)
print("Angle between is:", Vec3.angle_between(x,y),f"/n Added they are:", Vec3.add(x,y), f"/n And their displacement is:", Vec3.disp(x,y))