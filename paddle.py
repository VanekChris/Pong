import pygame

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def move(self, s):
        self.rect.y += s
        if self.rect.y <= 50:
            self.rect.y = 50
        if self.rect.bottom >= 600:
            self.rect.bottom= 600