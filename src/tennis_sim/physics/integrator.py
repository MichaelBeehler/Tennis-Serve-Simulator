# Update characteristics as time passes

def euler_step(ball, ax, ay, dt):

    ball.vx += ax * dt
    ball.vy += ay * dt

    ball.x += ball.vx * dt
    ball.y += ball.vy * dt