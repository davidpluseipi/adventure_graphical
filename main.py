import math
import numpy as np
import pygame
import sys
import time
# from waiting import wait, TimeoutExpired


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

    def move(self):
        self.x += dx
        if self.x > width:
            self.x = width
        elif self.x < 0:
            self.x = 0

        self.y += dy
        if self.y > height:
            self.y = height
        elif self.y < 0:
            self.y = 0

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

    def randomize_info(self, bank_of_info_):
        i = np.random.randint(0, len(all_info) - 1)
        self.info = bank_of_info_[i]


class Gold:
    def __init__(self):
        self.gold = 100
        self.x = np.random.randint(1, width)
        self.y = np.random.randint(1, height)
        self.capture_radius = 50


def draw_text(text, font_, text_color, position):
    img = font_.render(text, True, text_color)
    screen.blit(img, (position[0], position[1]))


def look_for_sprite(player, sprite):
    distance = math.sqrt((player.x - sprite.x) ** 2 + (player.y - sprite.y) ** 2)

    # offset the fruit capture words based on player position
    if distance < sprite.capture_radius:

        if player.x < screen.get_width() / 2:
            offset[0] = spacing
        else:
            offset[0] = -spacing

        if player.y < screen.get_height() / 2:
            offset[1] = -spacing
        else:
            offset[1] = spacing

        draw_text(sprite.info, font, light_grey, (sprite.x + offset[0], sprite.y + offset[1]))

        pygame.display.update()


def look_for_gold(player, gold):
    distance = math.sqrt((player.x - gold.x) ** 2 + (player.y - gold.y) ** 2)

    if distance < gold.capture_radius:
        player1.take_gold(gold)


def capture_input(player, event_):
    global dx, dy
    if event_.key == pygame.K_LEFT:
        dx = -step
        dy = 0

    elif event_.key == pygame.K_RIGHT:
        dx = step
        dy = 0

    elif event_.key == pygame.K_DOWN:
        dx = 0
        dy = step

    elif event_.key == pygame.K_UP:
        dx = 0
        dy = -step

    elif event_.key == pygame.K_s:
        player.show_status()
        dx, dy = 0, 0

    return dx, dy


class Option:
    hovered = False

    def __init__(self, text, pos_):
        self.text = text
        self.pos_ = pos_
        self.rend = menu_font.render(self.text, True, self.get_color())
        self.rect = self.rend.get_rect()
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return 255, 255, 255
        else:
            return 100, 100, 100

    def set_rect(self):
        self.set_rend()
        self.rect.topleft = self.pos_

    def is_clicked(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


# Main

# Local Variables
fps = 15
game_over = False
offset = [0, 0]
spacing = 20
step = 20
timer_expired = False
dx, dy = 0, 0
width, height = 450, 450


# Pygame Setup
pygame.init()
clock = pygame.time.Clock()

# define fonts
font = pygame.font.SysFont('arial', 20)
menu_font = pygame.font.Font(None, 40)

# screen setup
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('bg.png')
screen.blit(bg, (0, 0))

# startup screen
options = [Option("New Game", (140, 100)),
           Option("Load Game", (140, 150)),
           Option("Options", (140, 200))]

# Create player(s)
player1 = Player()
player1_img = pygame.image.load('white_square.png')

# Create Sprites
sprite1 = Sprite()
sprite2 = Sprite()
sprite_img = pygame.image.load('green_square.png')

# Create pot(s) of gold
gold1 = Gold()
print(f"Gold1:  x: {gold1.x}, y: {gold1.y}")

# Create a 'list' of everything the sprites could say
all_info = ["I have nothing to say.",
            "I think you should go north.",
            "Try digging."]

# draw player1
screen.blit(player1_img, (player1.x, player1.y))

# set title bar caption
pygame.display.set_caption('Adventure')


# define colors
black = (0, 0, 0)
light_grey = (200, 200, 200)
red = (213, 50, 80)

# Optional timer
game_clock = 10 * 60  # 10 minutes
start_time = time.time()

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
        option.draw()

    pygame.display.update()

print(selection)
screen.blit(bg, (0, 0))
if selection == "New Game":
    draw_text("Starting...", menu_font, light_grey, (140, 100))

elif selection == "Load Game":
    draw_text(f"Unable to {selection}", menu_font, light_grey, (80, 100))
    draw_text("(Game still under development)", font, light_grey, (110, 200))

elif selection == "Options":
    draw_text(f"Unable to open {selection}", menu_font, light_grey, (70, 100))
    draw_text("(Game still under development)", font, light_grey, (110, 200))

pygame.display.update()
time.sleep(2)

del event
pygame.event.clear()
first_loop = True
key_up = False

while not game_over:

    # draw background
    screen.blit(bg, (0, 0))

    # this prevents it from waiting for input with a blank screen on startup
    if 'first_loop' in locals():
        screen.blit(player1_img, (player1.x, player1.y))

        draw_text("Player 1", font, light_grey, (5, height - 60))
        draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30))

        # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
        # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

        pygame.display.update()
        del first_loop

    # wait for an event
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        game_over = True
    elif event.type == pygame.KEYUP:
        key_up = True
    elif event.type == pygame.KEYDOWN:
        dx, dy = capture_input(player1, event)

    # Move and draw player1
    if not key_up:
        player1.move()
    else:
        key_up = False

    screen.blit(player1_img, (player1.x, player1.y))

    # calculate the distance between a player and sprite and, if close, print the sprite's info
    look_for_sprite(player1, sprite1)

    # calculate the distance between a player and a pot of gold and, if close, take the gold
    look_for_gold(player1, gold1)

    # # Randomize the sprite's info
    # if player1.x == sprite1.x and player1.y == sprite1.y:
    #     sprite1.randomize_info(all_info)
    #     print(f"A sprite has appeared. It says '{sprite1.info}'")

    if time.time() > (start_time + game_clock) and timer_expired is False:
        print('Timer expired')
        timer_expired = True

    draw_text("Player 1", font, light_grey, (5, height - 60))
    draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30))

    # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
    # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

    # update the screen
    pygame.display.update()

pygame.quit()
sys.exit()
