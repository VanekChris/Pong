import pygame

class TextRect(pygame.sprite.Sprite):

    def __init__(self, x, y, text, font_size, color):
        super().__init__()
        self.font = pygame.font.Font("font/PublicPixel.ttf", font_size)
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def position(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]

    def update(self, new_score):
        self.text = "Score: " + str(new_score)
        self.image = self.font.render(self.text, True, self.color)