# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


color = (255,0,0)


class Player():
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
    def move(self):
        if (self.x + self.moving["x"]) > 0 and (self.x + self.moving["x"] < 1280):
            self.x += self.moving["x"]

    def draw_player(self):
        player = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, player)

player = Player()

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        dx = 0
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                dx = -5
            elif event.key==pygame.K_RIGHT:
                dx = 5
        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                dx = 0
            elif event.key==pygame.K_RIGHT:
                dx = 0
        player.moving["x"] = dx
    

    # RENDER YOUR GAME HERE
    player.move()
    player.draw_player()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
