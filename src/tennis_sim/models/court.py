class Court:
    def __init__(self, surface="hard"):
        self.surface = surface

        # Geometry of the court
        self.net_height = 0.914 # m, assumung center of net
        self.net_position = 11.89 # m, distance between baseline and net
        self.service_line = 18.29 # m, distance from server's baseline to opponent's service line

        # Court properties
        self.friction = self.get_friction()
        self.restitution = self.get_restitution()

        def get_friction ():
            """
            Horizontal speed reduction during bounce.
            """
            values = {
                "hard": 0.80,
                "grass": 0.90,
                "clay": 0.70
            }

            return values[self.surface]

        def get_restitution ():
            """
            Bounce energy retention coefficient.
            Higher = bouncier surface.
            """
            values = {
                "hard": 0.75,
                "clay": 0.70,
                "grass": 0.60
            }
            return values[self.surface]