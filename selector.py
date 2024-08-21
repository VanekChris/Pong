import pygame

class SelectRect(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y, width, height, b):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        rect = pygame.Rect(0, 0, width, height)
        pygame.draw.rect(self.image, color, rect, b)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def update(self):
        pass