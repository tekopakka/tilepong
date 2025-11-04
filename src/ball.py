import pygame
import player

class Ball:
    def __init__(self, player, target):
        self.x = 100
        self.y = 300
        self.radius = 5
        self.color = (0,255,0)
        self.moving = {
            "x": 2,
            "y": 4
        }
        self.player = player
        self.target = target
        
    def collision_x(self):
        return self.x + self.moving["x"] >= 1270 or \
            self.x + self.moving["x"] <= 10
    def collision_y(self):
        return self.y + self.moving["y"] >= 710 or \
            self.y + self.moving["y"] <= 10
    def collision_player(self):
        return self.x > self.player.x and \
            self.x < (self.player.x + self.player.width) and \
            (self.y == self.player.y - 1 or \
            self.y == self.player.y or \
            self.y == self.player.y + 1)
    
    def collision_target_tile(self):
        for tilerow in self.target.tiles:
            for tile in tilerow:
                if tile.exists:
                    if self.x >= tile.x and self.x <= (tile.x + tile.width) \
                    and self.y <= (tile.y + tile.height) and self.y >= tile.y:
                        tile.exists = False
                        return True
        return False
                        
    def bounce_off(self):
        self.moving["y"] *= -1
                    

    def move(self):
        if (self.x + self.moving["x"]) > 10 \
            and (self.x + self.moving["x"] < 1270):
            self.x += self.moving["x"]
        if  (self.y + self.moving["y"]) < 710:
            self.y += self.moving["y"]
            
        if self.collision_x():
            self.moving["x"] *= -1
        if self.collision_y():
            self.moving["y"] *= -1
        elif self.collision_player():
            self.change_ball_movement()
        elif self.collision_target_tile():
            self.bounce_off()

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, width=0)

    def change_ball_movement(self):
        self.moving["y"] *= -1
        hitspot = self.x - (self.player.x + self.player.width/2)
        print(hitspot)
        print(abs(hitspot))
        if hitspot == 0:
            print("Middle shot")
        elif abs(hitspot) < 10:
            self.moving["x"] += abs(hitspot)/hitspot
        elif abs(hitspot) >= 10 and abs(hitspot) <= 30:
            multiplier = 2
            if self.moving["x"] > 0 and hitspot < 0 \
            or self.moving["x"] < 0 and hitspot > 0:
                multiplier = 4
            self.moving["x"] += multiplier*abs(hitspot)/hitspot
        elif abs(hitspot) >= 30 and abs(hitspot) < 50:
            multiplier = 3
            if self.moving["x"] > 0 and hitspot < 0 \
                or self.moving["x"] < 0 and hitspot > 0:
                multiplier = 6
                self.moving["x"] += multiplier*abs(hitspot)/hitspot
    
        print("Ball speed", self.moving["x"])