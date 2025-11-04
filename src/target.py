import pygame

class Tile:
    def __init__(self, w, h, x, y, exists=True):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.exists = exists
        self.color = (55,100,255)

class Target:
    def __init__(self):
        self.tiles = []

    def generate_tiles(self):
        y = 20
        while y < 300:
            tile_row = []
            x = 20
            while x < 1280:
                tile = Tile(50, 10, x, y)
                tile_row.append(tile)
                x += (10 + tile.width)
            y += (10 + tile.height)
            self.tiles.append(tile_row)
    
    def draw_tile_grid(self, screen):
        for tiles_line in self.tiles:
            for tile in tiles_line:
                if tile.exists:
                    t = pygame.Rect((tile.x, tile.y, tile.width, tile.height))
                    pygame.draw.rect(screen, tile.color, t)