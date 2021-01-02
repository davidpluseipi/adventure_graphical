import numpy as np
import pygame


class Sprite:
    def __init__(self):
        self.speed = 5
        self.info = "Hi there!"
        self.x = 50
        self.y = 50
        self.capture_radius = 10
        self.image_path = "images/green_square.png"
        self.image = self.load_image()

    def randomize_info(self, bank_of_info_):
        i = np.random.randint(0, len(bank_of_info_) - 1)
        self.info = bank_of_info_[i]

    def load_image(self):
        return pygame.image.load(self.image_path).convert()  # loads and converts to pixel format of display




