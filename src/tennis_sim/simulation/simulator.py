from tennis_sim.models.ball import Ball
from tennis_sim.physics.integrator import euler_step
from tennis_sim.physics.constants import GRAVITY, NET_HEIGHT, NET_POSITION, SERVICE_LINE


def simulate (ball, dt=0.01, max_time=5):

    positions = []

    t = 0.0

    while t < max_time and ball.y >= 0:
        ax = 0
        ay = -GRAVITY

        euler_step(ball, ax, ay, dt)

        positions.append((ball.x, ball.y))

        print (f'Time {t:.2f} - X: {ball.x}m, Y: {ball.y}m')

        if ball.y <= NET_HEIGHT and ball.x <= NET_POSITION:
            return positions, 'Hits Net - Fault'

        elif ball.y >=0 and ball.x > SERVICE_LINE:
            return positions, 'Long - Fault'


        t += dt

    return positions, 'In Box'