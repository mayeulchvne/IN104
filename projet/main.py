#!/usr/bin/env python3

from simulator import Simulator, World, Body
from simulator.utils.vector import Vector2
from simulator.solvers import DummySolver
from simulator.physics.engine import DummyEngine
from simulator.graphics import Screen

import pygame as pg

if __name__ == "__main__":
    b1 = Body(Vector2(0, 0),
              velocity=Vector2(-3, -3),
              mass=10,
              draw_radius=10)
    b2 = Body(Vector2(2, 2),
              velocity=Vector2(0, 0),
              mass=1,
              draw_radius=5)
    b3 = Body(Vector2(-1, -3),
              velocity=Vector2(0, 0),
              mass=5,
              draw_radius=7)
    b4 = Body(Vector2(1, 3),
              velocity=Vector2(0, 0),
              mass=3,
              draw_radius=3)
    b5 = Body(Vector2(-4, 2),
              velocity=Vector2(0, 0),
              mass=6,
              draw_radius=8)

    world = World()
    world.add(b1)
    world.add(b2)
    world.add(b3)
    world.add(b4)
    world.add(b5)

    simulator = Simulator(world, DummyEngine, DummySolver)

    screen_size = Vector2(800, 600)
    screen = Screen(screen_size,
                    bg_color=(0, 0, 0),
                    caption="Simulator")
    screen.camera.scale = 50

    # this coefficient controls the speed
    # of the simulation
    time_scale = 10

    print("Start program")
    while not screen.should_quit:
        dt = screen.tick(60)

        # simulate physics
        delta_time = time_scale * dt / 1000
        simulator.step(delta_time)

        # read events
        screen.get_events()

        # handle events
        #   scroll wheel
        if screen.get_wheel_up():
            screen.camera.scale *= 1.1
        elif screen.get_wheel_down():
            screen.camera.scale *= 0.9

        # draw current state
        screen.draw(world)

        # draw additional stuff
        screen.draw_corner_text("Time: %f" % simulator.t)

        # show new state
        screen.update()

    screen.close()
    print("Done")
