import pygame


class Option:
    # hovered = False

    def __init__(self, text, pos, menu_font, screen):
        self.text = text
        self.pos = pos
        self.font = menu_font
        self.hovered = False
        self.rend = self.font.render(self.text, True, self.get_color())
        self.rect = self.rend.get_rect()
        self.set_rect()
        self.draw(screen)

    def draw(self, screen_):
        self.set_rend()
        screen_.blit(self.rend, self.rect)

    def set_rend(self, ):
        self.rend = self.font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return 255, 255, 255
        else:
            return 100, 100, 100

    def set_rect(self):
        self.set_rend()
        self.rect.topleft = self.pos

    def is_clicked(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False
