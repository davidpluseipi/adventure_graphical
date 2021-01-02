import pygame


def capture_key_down(player):

    keys = pygame.key.get_pressed()
    player.up, player.down, player.left, player.right = [False, False, False, False]

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.left = True

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.right = True

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.down = True

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player.up = True

    elif keys[pygame.K_1]:
        player.show_status()

    return player




