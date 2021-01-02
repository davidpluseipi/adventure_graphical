import math
import pygame
from draw_text import *


def look_for_sprite(player, sprite, game_data):
    [screen, font, color] = game_data
    spacing = 20
    distance = math.sqrt((player.x - sprite.x) ** 2 + (player.y - sprite.y) ** 2)
    offset = [0, 0]

    if distance < sprite.capture_radius:

        if player.x < screen.get_width() / 2:
            offset[0] = spacing
        else:
            offset[0] = -(spacing + 50)

        if player.y > spacing:
            offset[1] = -spacing
        else:
            offset[1] = spacing

        draw_text(sprite.info, font, color, (sprite.x + offset[0], sprite.y + offset[1]), screen)

        pygame.display.update()
