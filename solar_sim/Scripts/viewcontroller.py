#https://stackoverflow.com/questions/38118598/how-to-create-a-3d-animation
import matplotlib.pyplot as plt
from model import Simulation
import params
from time import time_ns

NS_TO_MS = 1000000

class ViewController:
    model: Simulation
    
    def __init__(self, model: Simulation) -> None:
        self.model = model
        self.simtime = params.simtime
        self.ticks = params.simtime/params.time_step
        
    def start_sim(self) -> None:
        self.tickcount = 0
        self.tick()
        
        pass
    
    def tick(self) ->None:
        self.model.tick()
        
        #Check if sim is finished
        if self.model.finished:
            return
        
        else:
            #Continue drawing graphs
                a =1