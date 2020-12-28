import math
import numpy as np
import pygame
import sys
import time
# from waiting import wait, TimeoutExpired


# Define Global Variables

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
        self.image_path = "white_square.png"  # path to image_path file
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

    def move(self):
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
        self.image = "green_square.png"

    def randomize_info(self, bank_of_info_):
        i = np.random.randint(0, len(all_info) - 1)
        self.info = bank_of_info_[i]

    def load_image(self):
        return pygame.image.load(self.image).convert()  # loads and converts to pixel format of display


class Gold:
    def __init__(self):
        self.gold = 100
        self.x = np.random.randint(1, width)
        self.y = np.random.randint(1, height)
        self.capture_radius = 100


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
            offset[0] = -(spacing + 50)

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


def capture_key_up():
    global move_left, move_right, move_up, move_down
    move_left, move_right, move_up, move_down = False, False, False, False


def capture_key_down(player):
    global dx, dy, move_left, move_right, move_up, move_down

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_right = False
        move_left = True
        # dx = -step
        # dy = 0

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_left = False
        move_right = True
        # dx = step
        # dy = 0

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_up = False
        move_down = True
        # dx = 0
        # dy = step

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        move_down = False
        move_up = True
        # dx = 0
        # dy = -step

    # elif event_.key == pygame.K_UP:
    #     dx = 0
    #     dy = -step

    elif keys[pygame.K_1]:
        player.show_status()


# Main
# Local Variables
fps = 15
game_over = False
last_key = None
offset = [0, 0]
spacing = 20
step = 1
full_grown = False
dx, dy = 0, 0
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
bg = pygame.image.load('bg.png')
screen.blit(bg, (0, 0))

# startup screen
options = [Option("New Game", (140, 100)),
           Option("Load Game", (140, 150)),
           Option("Options", (140, 200))]

# Create player(s)

# Create the player1 object based on the Player Class
player1 = Player("v00d00Master")

# Define the path to the image_path that will be associated with player1
player1.image_path = 'rick_thinking_small.png'

# Create an image_path object from file location stored in player.image_path
player1.img = player1.load_image()

# draw player1
screen.blit(player1.img, (player1.x, player1.y))

# Create Sprites
sprite1 = Sprite()
sprite1.x, sprite1.y = 100, 100
sprite1_img = pygame.image.load(sprite1.image)
screen.blit(sprite1_img, (sprite1.x, sprite1.y))

sprite2 = Sprite()
sprite2.x, sprite2.y = 400, 300
sprite2.image = "white_square.png"
sprite2_img = pygame.image.load(sprite2.image)
screen.blit(sprite2_img, (sprite2.x, sprite2.y))


# Create pot(s) of gold
gold1 = Gold()
print(f"Gold1:  x: {gold1.x}, y: {gold1.y}")

# Create a 'list' of everything the sprites could say
all_info = ["I have nothing to say.",
            "I think you should go north.",
            "Try digging.",
            """It's a figure of speech, Morty. They're bureaucrats. 
            I don't respect them. Just keep shooting!"""]

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

# Prep to detect holding down a key as repeated down presses
pygame.key.set_repeat(5)  # stops the player when you stop pressing keys

# Optional timer
seconds_per_year = 1 * 60  # seconds
start_time = time.time()  # seconds since some day in 1970
age = 1

while not game_over:
    # draw background
    screen.blit(bg, (0, 0))

    # this prevents it from waiting for input with a blank screen on startup
    if 'first_loop' in locals():
        screen.blit(player1.img, (player1.x, player1.y))

        draw_text("Player 1", font, light_grey, (5, height - 60))
        draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30))

        # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
        # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

        pygame.display.update()
        del first_loop

    # blocks interference from hovering the mouse over the game
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    # wait for an event
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        game_over = True

    elif event.type == pygame.KEYUP:
        capture_key_up()
        # dx, dy = 0, 0

    elif event.type == pygame.KEYDOWN:
        capture_key_down(player1)

    player1.move()

    screen.blit(player1.img, (player1.x, player1.y))
    screen.blit(sprite1_img, (sprite1.x, sprite1.y))
    screen.blit(sprite2_img, (sprite2.x, sprite2.y))

    # calculate the distance between a player and sprite and, if close, print the sprite's info
    look_for_sprite(player1, sprite1)
    look_for_sprite(player1, sprite2)

    # calculate the distance between a player and a pot of gold and, if close, take the gold
    look_for_gold(player1, gold1)

    # # Randomize the sprite's info
    # if player1.x == sprite1.x and player1.y == sprite1.y:
    #     sprite1.randomize_info(all_info)
    #     print(f"A sprite has appeared. It says '{sprite1.info}'")

    # age and grow taller and stronger every "year"
    if time.time() > (start_time + age * seconds_per_year) and full_grown is False:
        player1.grow_taller()
        player1.show_status()
        age += 1
        if age >= 18:
            full_grown = True

    draw_text("Player 1", font, light_grey, (5, height - 60))
    draw_text(f"Gold: {player1.gold}", font, light_grey, (5, height - 30))

    # draw_text("Player 2", font, light_grey, (width - 75, height - 60))
    # draw_text(f"Gold: {player1.gold}", font, light_grey, (width - 75, height - 30))

    # update the screen
    pygame.display.update()

    # pygame.time.delay(10)

pygame.quit()
sys.exit()
