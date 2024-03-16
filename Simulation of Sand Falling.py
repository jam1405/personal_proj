#Simulation of Sand Falling
#   A number of sand particles are dropped into a triangular basin
#   Within the basin are a number of levels, with each level having an increasing number of pins for the sand to bounce off of
#   1st level = 1 pin, 2nd level = 2pins, 3rd level = 4pins
#   Pins(level) = level
#   Each pin causes a 50/50 random split of sand trajectories
#   Sand ends up in one of many final bins, Bins(level) = level + 1   

#Packages 
import random as r
import numpy as np
import matplotlib.pyplot as plt

#Define experiment
class SandExperiment:
    
    def __init__(self, num_sand, levels):
        self.count = num_sand
        self.levels = levels
    

    
def get_user_input():
    sand = int(input("How many particles of sand for the simulation? :"))
    levels = int(input("How many levels in the simulation? :"))
    return sand, levels
    
def sim():
    #setup
    num_sand , levels = get_user_input()
    finalpos = np.ones(num_sand,dtype = int)
    
    #Sim
    exp = SandExperiment(num_sand,levels)
    
    #Generate Final positions of sand after falling
    for i in range(exp.count):
        for j in range(exp.levels):
            finalpos[i] = finalpos[i]+ r.randint(0,1)
    
    #Count how many sand grains landed in each bin
    unique, counts = np.unique(finalpos, return_counts = True)
    Dist = dict(zip(unique,counts))
    
    Bins = list(Dist.keys())
    Counts = list(Dist.values())
    return Bins, Counts , len(Dist)
    
def main():
    Bins, Counts, length = sim()
    
    #Graphing
    plt.bar(range(length), Counts,tick_label=Bins)
    plt.xlabel("Bin")
    plt.ylabel("Number of Sand Particles")
    plt.title("Distribution of Sand across Bins")
    plt.show()
        
if __name__ == '__main__':
    main()