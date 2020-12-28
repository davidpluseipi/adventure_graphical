import sys
import time
from classes import *
from functions import *


# Main
# Local Variables
fps = 15
game_over = False
last_key = None
offset = [0, 0]
spacing = 20
step = 1
full_grown = False
width, height = 450, 450
move_left, move_right, move_up, move_down = False, False, False, False

# Pygame Setup
pygame.init()
clock = pygame.time.Clock()

# define fonts
font = pygame.font.SysFont('arial', 20)
menu_font = pygame.font.Font(None, 40)

# screen setup
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()  # needed for clamp_ip to keep player on the screen
bg = pygame.image.load('images/bg.png')
screen.blit(bg, (0, 0))

# startup screen
options = [Option("New Game", (140, 100), menu_font, screen),
           Option("Load Game", (140, 150), menu_font, screen),
           Option("Options", (140, 200), menu_font, screen)]

# Create player(s)
# Create the player1 object based on the Player Class
player1 = Player("v00d00Master")

# Define the path to the image_path that will be associated with player1
player1.image_path = 'images/rick_thinking_small.png'

# Create an image_path object from file location stored in player.image_path
player1.img = player1.load_image()

# draw player1
screen.blit(player1.img, (player1.x, player1.y))

# Create Sprites
# Create a 'list' of everything the sprites could say
all_info = ["I have nothing to say.",
            "I think you should go north.",
            "Try digging.",
            """It's a figure of speech, Morty. They're bureaucrats. 
            I don't respect them. Just keep shooting!"""]

sprite1 = Sprite()
sprite1.x, sprite1.y = 100, 100
sprite1_img = pygame.image.load(sprite1.image)
screen.blit(sprite1_img, (sprite1.x, sprite1.y))

sprite2 = Sprite()
sprite2.x, sprite2.y = 400, 300
sprite2.image = "images/white_square.png"
sprite2_img = pygame.image.load(sprite2.image)
screen.blit(sprite2_img, (sprite2.x, sprite2.y))
sprite2.randomize_info(all_info)


# Create pot(s) of gold
gold1 = Gold(width, height)
gold2 = Gold(width, height)
print(f"Gold1:  x: {gold1.x}, y: {gold1.y}")
print(f"Gold2:  x: {gold2.x}, y: {gold2.y}")


# set title bar caption
pygame.display.set_caption('adventure')

# define colors
black = (0, 0, 0)
light_grey = (200, 200, 200)
red = (213, 50, 80)

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
pygame.event.clear()
first_loop = True
key_up = False

# Prep to detect holding down a key as repeated down presses
pygame.key.set_repeat(5)  # stops the player when you stop pressing keys

# Timer that ages the character
seconds_per_year = 1 * 60  # seconds
start_time = time.time()  # seconds since some day in 1970
age = 1  # starting age


while not game_over:
    # blocks interference from hovering the mouse over the game
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    # draw background
    screen.blit(bg, (0, 0))

    # this prevents it from waiting for input with a blank screen on startup
    if 'first_loop' in locals():
        screen.blit(player1.img, (player1.x, player1.y))

        # display stats for player1
        draw_text("Player 1", font, light_grey, (5, height - 60), screen)
        draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30), screen)

        # display stats for player2
        # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
        # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

        pygame.display.update()
        del first_loop

    # wait for an event
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        game_over = True

    elif event.type == pygame.KEYUP:
        capture_key_up(move_left,
                       move_right,
                       move_up,
                       move_down)

    elif event.type == pygame.KEYDOWN:
        move_left, move_right, move_up, move_down = capture_key_down(move_left,
                                                                     move_right,
                                                                     move_up,
                                                                     move_down,
                                                                     player1)

    # move the player
    player1.move(move_up,
                 move_down,
                 move_left,
                 move_right,
                 width,
                 height,
                 step)

    # draw each of the characters
    screen.blit(player1.img, (player1.x, player1.y))
    screen.blit(sprite1_img, (sprite1.x, sprite1.y))
    screen.blit(sprite2_img, (sprite2.x, sprite2.y))

    # calculate the distance between a player and sprite and, if close, print the sprite's info
    game_data = [screen, offset, spacing, font, light_grey]
    look_for_sprite(player1, sprite1, game_data)
    look_for_sprite(player1, sprite2, game_data)

    # calculate the distance between a player and a pot of gold and, if close, take the gold
    look_for_gold(player1, gold1)

    # age and grow taller and stronger every "year"
    if time.time() > (start_time + age * seconds_per_year) and full_grown is False:
        player1.grow_taller()
        player1.show_status()
        age += 1
        if age >= 18:
            full_grown = True

    draw_text("Player 1", font, light_grey, (5, height - 60), screen)
    draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30), screen)

    # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
    # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

    # update the screen
    pygame.display.update()

pygame.quit()
sys.exit()
