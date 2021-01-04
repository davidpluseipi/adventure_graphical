import pygame


class Player:
    def __init__(self, name):
        self.name = name
        self.height = 5
        self.strength = 0
        self.wisdom = 0
        self.x = 0
        self.y = 0
        self.step = 1
        self.gold = 0
        self.image_path = ["images/white_square.png",  # up
                           "images/white_square.png",  # down
                           "images/white_square.png",  # left
                           "images/white_square.png"]  # right
        self.current_image = 1
        self.image = self.load_image()  # image_path object
        self.age = 1
        self.full_grown = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def load_image(self):
        return pygame.image.load(self.image_path[self.current_image]).convert()  # loads and converts to pixel format
        # of display

    def show_status(self):
        print(f"\n{self.name}")
        print("Strength: {0}".format(self.strength))
        print("Wisdom: {0}".format(self.wisdom))
        print("Gold: {0}".format(self.gold))

    def grow_taller(self):
        if self.height < 6:
            self.height += 0.1
            self.strength += 10

    def move(self, width, height):
        if self.up and self.y > 0:
            self.y -= self.step

        if self.down and self.y < (height - self.image.get_height()):
            self.y += self.step

        if self.left and self.x > 0:
            self.x -= self.step

        if self.right and self.x < (width - self.image.get_width()):
            self.x += self.step

    def take_gold(self, other):
        self.gold += other.gold
        other.gold = 0
