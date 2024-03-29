from turtle import Turtle, Screen, done
from model import Simulation
import params
from typing import Any
from time import time_ns


NS_TO_MS: int = 1000000

class ViewController:
    """This class is responsible for controlling the simulation and visualizing it."""
    screen: Any
    pen: Turtle
    model: Simulation

    def __init__(self, model: Simulation):
        """Initialize the VC."""
        self.model = model
        self.screen = Screen()
        self.screen.setup(params.VIEW_WIDTH, params.VIEW_HEIGHT)
        self.screen.tracer(0, 0)
        self.screen.delay(0)
        self.screen.title("Coulombic Particle Simulation")
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)

    def start_simulation(self) -> None:
        """Call the first tick of the simulation and begin turtle gfx."""
        self.tick()
        done()

    def tick(self) -> None:
        """Update the model state and redraw visualization."""
        start_time = time_ns() // NS_TO_MS
        self.model.tick()
        self.pen.clear()
        for particle in self.model.population:
            self.pen.penup()
            self.pen.goto(particle.loc.x, particle.loc.y)
            self.pen.pendown()
            self.pen.color(particle.color())
            self.pen.dot(params.PARTICLE_RADIUS)
        self.screen.update()

        if self.model.is_complete():
            return
        else:
            end_time = time_ns() // NS_TO_MS
            next_tick = 30 - (end_time - start_time)
            if next_tick < 0:
                next_tick = 0
            self.screen.ontimer(self.tick, next_tick)