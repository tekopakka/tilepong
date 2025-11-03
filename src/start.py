import pygame
from player import Player
from ball import Ball

def run():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    player = Player()
    ball = Ball(player)

    while running:
        screen.fill("white")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
            player.moving["x"] = dx
        

        player.move()
        ball.move()
        player.draw_player(screen)
        ball.draw_ball(screen)

        if ball.y > 700:
            print("GAME OVER")
            break

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
