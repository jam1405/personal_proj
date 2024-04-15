#https://stackoverflow.com/questions/38118598/how-to-create-a-3d-animation
import matplotlib.pyplot as plt
from model import Simulation, Vec3
import params




class ViewController:
    model: Simulation
    
    def __init__(self, model: Simulation) -> None:
        self.model = model
        self.simtime = params.simtime
        self.ticks_total = params.ticks
        
        
    def start_sim(self) -> None:
        #Initialize graph axes and labels?
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection = '3d')
        self.ax.scatter([0,1,2], [2,4,6], [6,7,8])
        plt.clf()
        self.run_sim()
        
    
    def run_sim(self):
        print("##########RUNNING SOLAR SYSTEM SIMULATION##########")
        print("Total Simulated Time: {time} days".format(time = params.simtime))
        for tick in self.ticks_total:
            self.model.tick()
            if tick%50 == 0:
                print("{percent} {sign} simulated".format(percent = tick//params.ticks, sign = "%"))

        self.visualize()
        
    
    def visualize(self) -> None:
        time_count_msg:str = "{time} days since beginning"
        size = self.model.bodies[:,2]
        colours = self.model.bodies[:,9]
        for tick in self.ticks_total:
            plt.clf() #CLEAR FIGURE BEFORE PLOTTING
            
            tick_data: list[Vec3] = self.model.poslist[tick] #Data for this tick
            time_count_msg.format(time = tick*params.time_step) #Time counter msg for this tick
            
            #Graph with self.model.poslist(tick) for each ticks updated data
            self.ax.scatter(tick_data[:,0],tick_data[:,1],tick_data[:,2], s = size, c = colours, marker = "o") #Graph Scatterplot of data points
            #planet labels, time counter in top corner
            
            
            #Logic behind graph should be : 
            #CLEAR GRAPH -> Input tick data -> Draw data with spheres at pos -> Label spheres -> update time counter
            # CLEAR GRAPH FOR NEXT TICK but without losing labels or time counter