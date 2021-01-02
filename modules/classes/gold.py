import numpy as np


class Gold:
    def __init__(self, width, height):
        super(Gold, self).__init__()
        self.gold = 100
        self.x = np.random.randint(1, width)
        self.y = np.random.randint(1, height)
        self.capture_radius = 100
