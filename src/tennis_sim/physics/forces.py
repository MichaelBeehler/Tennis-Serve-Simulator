# Forces acting within our simulation
from .constants import GRAVITY as g

def gravity_force (m):
    return - (m * g)