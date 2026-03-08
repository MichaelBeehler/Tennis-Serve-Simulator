import numpy as np

from tennis_sim.models.ball import Ball
from tennis_sim.models.court import Court
from tennis_sim.simulation.simulator import simulate
from tennis_sim.visualization.plotter import plot_trajectory

speed = 15
angle = np.radians(3)

vx = speed * np.cos(angle)
vy = speed * np.sin(angle)

ball = Ball(0, 2.5, vx, vy)
court = Court('grass')

points, status = simulate(ball)


plot_trajectory(points)
print(status)