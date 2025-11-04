import pygame

class Player:
    def __init__(self):
        self.x = 200
        self.y = 600
        self.width = 100
        self.height = 10
        self.color = (255, 0, 0)
        self.moving = {
            "x": 0,
            "y": 0
        }

    def handle_movement(self, event):
        dx = 0
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                dx = -5
            if event.key==pygame.K_RIGHT:
                dx = 5
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                dx = 0
            if event.key==pygame.K_RIGHT:
                dx = 0
        self.moving["x"] = dx

    def move(self):
        if (self.x + self.moving["x"]) > 0 and (self.x + self.moving["x"] < 1280):
            self.x += self.moving["x"]

    def draw_player(self, screen):
        player = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, player)

