from viewcontroller import ViewController
from model import Simulation
import params
"__main__.py: Runs the solar simulation scripts from model.py through a visualizer: viewcontroller.py, using inputs from params.py"
__author__      = "Jamie Farquharson"
__copyright__   = "No copyright, feel free to use as you please :)"

"Credit to JPL Horizons for initial position and velocity data for the various planets."

def main() -> None:
    bodies = [
        params.sun_data,
        params.merc_data,
        params.ven_data,
        params.ear_data,
        params.mars_data,
        params.jup_data,
        params.sat_data,
        params.uran_data,
        params.nept_data,
        params.plut_data
    ]
    sim = Simulation(bodies)
    vc = ViewController(sim)
    vc.start_sim()
    return

if __name__  == "__main__":
    main()