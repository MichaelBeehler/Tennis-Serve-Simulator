import matplotlib.pyplot as plt

def plot_trajectory(points):

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.plot(xs, ys)
    plt.xlabel('Distance [m]')
    plt.ylabel('Height [m]')
    plt.title('Serve Trajectory')

    plt.axhline(0)
    plt.show()