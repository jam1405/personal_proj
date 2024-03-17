
import params
from model import Simulation
from viewcontroller import ViewController

#Dependencies
#math --> pi, cos, sin, atan2
#random --> getrandbit, random, randint
#turtle
#typing --> List 
    
        
        
        
# https://stackoverflow.com/questions/27820447/how-should-i-go-about-animating-particles-in-python-matplotlib

#Setting up animation
def main() -> None:
    model = Simulation(params.PARTICLE_COUNT)
    vc = ViewController(model)
    vc.start_simulation()
    
if __name__ == '__main__':
    main()