from setup import *
from option import Option
from draw_text import *
import time

# Starting Menu
options = [Option("New Game", (140, 100), menu_font, screen),
           Option("Load Game", (140, 150), menu_font, screen),
           Option("Options", (140, 200), menu_font, screen)]
selection = " "
selection_made = False

while not selection_made:
    event = pygame.event.wait()
    screen.fill((0, 0, 0))

    if event.type == pygame.QUIT:
        selection_made = True
        game_over = True

    elif event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()

    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
            if option.is_clicked() is True:
                selection = option.text
                selection_made = True
                break
        else:
            option.hovered = False
        option.draw(screen)

    pygame.display.update()
screen.blit(bg, (0, 0))

if selection == "New Game":
    draw_text("Starting...", menu_font, light_grey, (140, 100), screen)

elif selection == "Load Game":
    draw_text(f"Unable to {selection}", menu_font, light_grey, (80, 100), screen)
    draw_text("(Game still under development)", font, light_grey, (110, 200), screen)

elif selection == "Options":
    draw_text(f"Unable to open {selection}", menu_font, light_grey, (70, 100), screen)
    draw_text("(Game still under development)", font, light_grey, (110, 200), screen)

pygame.display.update()
time.sleep(2)
del event
