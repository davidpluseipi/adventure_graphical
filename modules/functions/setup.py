from gold import Gold
from player import Player
from sprite import Sprite
import pygame


width, height = 640, 480

# Pygame Setup
pygame.init()

# define fonts
font = pygame.font.SysFont('arial', 20)
menu_font = pygame.font.Font(None, 40)

# screen setup
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()  # needed for clamp_ip to keep player on the screen
bg = pygame.image.load('images/bg.png')
screen.blit(bg, (0, 0))

# set title bar caption
pygame.display.set_caption('adventure')

# define colors
black = (0, 0, 0)
light_grey = (200, 200, 200)
red = (213, 50, 80)

# Create player(s)
player1 = Player("v00d00Master")

# Define the path to the image_path that will be associated with player1
player1.image_path = 'images/rick_thinking_small.png'
player1.image = player1.load_image()

# Create a 'list' of everything the sprites could say
all_info = ["I have nothing to say.",
            "I think you should go north.",
            "Try digging.",
            """It's a figure of speech, Morty. They're bureaucrats. 
            I don't respect them. Just keep shooting!"""]

# Create Sprites
sprite1 = Sprite()
sprite1.x, sprite1.y = 100, 100
sprite1.image = sprite1.load_image()
screen.blit(sprite1.image, (sprite1.x, sprite1.y))

sprite2 = Sprite()
sprite2.x, sprite2.y = 400, 300
sprite2.image_path = "images/white_square.png"
sprite2.image = sprite2.load_image()
screen.blit(sprite2.image, (sprite2.x, sprite2.y))
sprite2.randomize_info(all_info)

# Create pot(s) of gold
gold1 = Gold(width, height)
gold2 = Gold(width, height)

# collect objects into lists
visible_things = [player1, sprite1, sprite2]
players = [player1]
sprites = [sprite1, sprite2]
golds = [gold1, gold2]
