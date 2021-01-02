import sys

# custom functions
from capture_key_down import *
from capture_key_up import *
from look_for_gold import *
from look_for_sprite import *

# custom scripts
from menu import *  # menu imports setup

# Main
print(f"Gold1:  x: {gold1.x}, y: {gold1.y}")
print(f"Gold2:  x: {gold2.x}, y: {gold2.y}")

# Prep to detect holding down a key as repeated down presses
pygame.key.set_repeat(5)

# Timer that ages the character
seconds_per_year = 1 * 60  # seconds
start_time = time.time()  # seconds since some day in 1970

first_loop = True
game_over = False
pygame.event.clear()

while not game_over:
    # draw background
    screen.blit(bg, (0, 0))

    # this prevents it from waiting for input with a blank screen on startup
    if 'first_loop' in locals():
        # draw each of the characters
        # noinspection PyUnboundLocalVariable
        screen.blit(player1.image, (player1.x, player1.y))
        screen.blit(sprite1.image, (sprite1.x, sprite1.y))
        screen.blit(sprite2.image, (sprite2.x, sprite2.y))

        # display stats for player1
        draw_text("Player 1", font, light_grey, (5, height - 60), screen)
        draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30), screen)

        # display stats for player2
        # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
        # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

        pygame.display.update()
        del first_loop

    # blocks interference from hovering the mouse over the game
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    # wait for event and capture input
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        game_over = True

    elif event.type == pygame.KEYUP:
        player1 = capture_key_up(player1)

    elif event.type == pygame.KEYDOWN:
        player1 = capture_key_down(player1)

    # move the player(s)
    for player in players:
        player.move(width, height)

    # draw each of the characters in their new position
    for thing in visible_things:
        screen.blit(thing.image, (thing.x, thing.y))

    # calculate the distance between a player and sprite and, if close, print the sprite's info
    game_data = [screen, font, light_grey]
    for player in players:

        # get info from sprites nearby
        for sprite in sprites:
            look_for_sprite(player, sprite, game_data)

        # collect any gold nearby
        for gold in golds:
            look_for_gold(player, gold)

        # age and grow taller and stronger every "year"
        if time.time() > (start_time + player.age * seconds_per_year) \
                and player.full_grown is False:
            player.grow_taller()
            player.show_status()
            player.age += 1
            if player.age >= 18:
                player.full_grown = True

    # Put stats on the screen
    draw_text("Player 1", font, light_grey, (5, height - 60), screen)
    draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30), screen)

    # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
    # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

    # update the screen
    pygame.display.update()

pygame.quit()
sys.exit()
