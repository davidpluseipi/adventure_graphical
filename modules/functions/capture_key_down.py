import pygame


def capture_key_down(player):

    keys = pygame.key.get_pressed()
    player.up, player.down, player.left, player.right = [False, False, False, False]
    previous_image = player.current_image

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.up = True
        player.current_image = 0

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.down = True
        player.current_image = 1

    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.left = True
        player.current_image = 2

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.right = True
        player.current_image = 3

    elif keys[pygame.K_1]:
        player.show_status()

    if previous_image != player.current_image:
        player.image = player.load_image()

    return player




