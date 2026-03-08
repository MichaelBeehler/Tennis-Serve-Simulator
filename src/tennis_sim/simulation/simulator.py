from tennis_sim.models.ball import Ball
from tennis_sim.physics.integrator import euler_step
from tennis_sim.physics.constants import GRAVITY


def simulate (ball, dt=0.01, max_time=5):

    positions = []

    t = 0.0

    while t < max_time and ball.y >= 0:
        ax = 0
        ay = -GRAVITY

        euler_step(ball, ax, ay, dt)

        positions.append((ball.x, ball.y))

        t += dt

    return positions