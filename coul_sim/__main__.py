from coul_sim import params
from coul_sim.model import Simulation
from coul_sim.viewcontroller import ViewController
    
        
        
        
        
# https://stackoverflow.com/questions/27820447/how-should-i-go-about-animating-particles-in-python-matplotlib

#Setting up animation
def main() -> None:
    model = Model(params.PARTICLE_COUNT, params.PARTICLE_SPEED)
    vc = ViewController(model)
    vc.start_simulation()
    
if __name__ == '__main__':
    main()