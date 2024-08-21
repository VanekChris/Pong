import pygame, random
pygame.mixer.init()
sfx = pygame.mixer.Sound("sound/pong.ogg")

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, x, y, r):
        self.reset(color, x, y, r)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.top <= 50 or self.rect.bottom >= 600:
            self.velocity[1] = -self.velocity[1]
            sfx.play()

        if self.rect.left <= 0:
            self.winner = 1

        if self.rect.right >= 600:
            self.winner = -1

        return self.winner

    def reset(self, color, x, y, r):
        super().__init__()
        self.image = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (r, r), r)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = random.choice([-1, 1])
        self.vertical = random.choice([-1, 1])
        self.velocity = [7 * self.direction, 7 * self.vertical]
        self.winner = 0