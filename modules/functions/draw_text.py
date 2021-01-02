def draw_text(text, font_, text_color, position, screen):
    img = font_.render(text, True, text_color)
    screen.blit(img, (position[0], position[1]))
