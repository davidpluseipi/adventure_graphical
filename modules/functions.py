import math
import pygame


def look_for_gold(player, gold):
    distance = math.sqrt((player.x - gold.x) ** 2 + (player.y - gold.y) ** 2)

    if distance < gold.capture_radius:
        player.take_gold(gold)


def look_for_sprite(player, sprite, game_data):
    [screen, offset, spacing, font, color] = game_data

    distance = math.sqrt((player.x - sprite.x) ** 2 + (player.y - sprite.y) ** 2)

    # offset the fruit capture words based on player position
    if distance < sprite.capture_radius:

        if player.x < screen.get_width() / 2:
            offset[0] = spacing
        else:
            offset[0] = -(spacing + 50)

        if player.y < screen.get_height() / 2:
            offset[1] = -spacing
        else:
            offset[1] = spacing

        draw_text(sprite.info, font, color, (sprite.x + offset[0], sprite.y + offset[1]), screen)

        pygame.display.update()


def capture_key_up(move_left, move_right, move_up, move_down):
    move_left, move_right, move_up, move_down = False, False, False, False
    return move_left, move_right, move_up, move_down


def capture_key_down(move_left, move_right, move_up, move_down, player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_up = False
        move_down = False
        move_left = True
        move_right = False

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_up = False
        move_down = False
        move_left = False
        move_right = True

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_up = False
        move_down = True
        move_left = False
        move_right = False

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        move_up = True
        move_down = False
        move_left = False
        move_right = False

    elif keys[pygame.K_1]:
        player.show_status()

    return move_left, move_right, move_up, move_down


def draw_text(text, font_, text_color, position, screen):
    img = font_.render(text, True, text_color)
    screen.blit(img, (position[0], position[1]))

