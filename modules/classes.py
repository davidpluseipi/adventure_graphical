import numpy as np
import pygame


# Define classes for each character type
class Player:
    def __init__(self, name):
        self.name = name
        self.height = 5
        self.strength = 0
        self.wisdom = 0
        self.x = 0
        self.y = 0
        self.gold = 0
        self.image_path = "images/white_square.png"  # path to image_path file
        self.img = self.load_image()  # image object

    def load_image(self):
        return pygame.image.load(self.image_path).convert()  # loads and converts to pixel format of display

    def show_status(self):
        print(f"\n{self.name}")
        # print("Height: {0}".format(self.height))
        print("Strength: {0}".format(self.strength))
        print("Wisdom: {0}".format(self.wisdom))
        print("Gold: {0}".format(self.gold))

    def grow_taller(self):
        if self.height < 6:
            self.height += 0.1
            self.strength += 10

    def move(self, move_up, move_down, move_left, move_right, width, height, step):
        if move_up and self.y > 0:
            self.y -= step

        if move_down and self.y < (height - self.img.get_height()):
            self.y += step

        if move_left and self.x > 0:
            self.x -= step

        if move_right and self.x < (width - self.img.get_width()):
            self.x += step

    def take_gold(self, other):
        self.gold += other.gold
        other.gold = 0


class Sprite:
    def __init__(self):
        self.speed = 5
        self.info = "Hi there!"
        self.x = 50
        self.y = 50
        self.capture_radius = 10
        self.image = "images/green_square.png"

    def randomize_info(self, bank_of_info_):
        i = np.random.randint(0, len(bank_of_info_) - 1)
        self.info = bank_of_info_[i]

    def load_image(self):
        return pygame.image.load(self.image).convert()  # loads and converts to pixel format of display


class Option:
    # hovered = False

    def __init__(self, text, pos, menu_font, screen):
        self.text = text
        self.pos = pos
        self.font = menu_font
        self.hovered = False
        self.rend = self.font.render(self.text, True, self.get_color())
        self.rect = self.rend.get_rect()
        self.set_rect()
        self.draw(screen)

    def draw(self, screen_):
        self.set_rend()
        screen_.blit(self.rend, self.rect)

    def set_rend(self, ):
        self.rend = self.font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return 255, 255, 255
        else:
            return 100, 100, 100

    def set_rect(self):
        self.set_rend()
        self.rect.topleft = self.pos

    def is_clicked(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


class Gold:
    def __init__(self, width, height):
        super(Gold, self).__init__()
        self.gold = 100
        self.x = np.random.randint(1, width)
        self.y = np.random.randint(1, height)
        self.capture_radius = 100
