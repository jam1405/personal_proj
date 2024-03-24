"""Constants used through the simulation."""

BOUNDS_WIDTH: float = float(input("How wide is the box? (INTEGER)"))
MAX_X: float = BOUNDS_WIDTH / 2
MIN_X: float = -MAX_X
VIEW_WIDTH: int = BOUNDS_WIDTH + 20

BOUNDS_HEIGHT: float = float(input("How high is the box? (INTEGER)"))
MAX_Y: float = BOUNDS_HEIGHT / 2
MIN_Y: float = -MAX_Y
VIEW_HEIGHT: int = BOUNDS_HEIGHT + 20

PARTICLE_RADIUS: int = 10
PARTICLE_COUNT: int = int(input("How many particles would you like in the box? (INTEGER)"))
CUTOFF_DIST:float = 30
MAX_SPEED: float = 1
SIM_TIME: int = 4000
TIME_STEP:float = 0.4
MASS = 1
STRENGTH = 30
REPULSION_STRENGTH = 0.2
