import pygame as pg
from map import *
from settings import *




class Minimap:
    def __init__(self,game):
        self.game = game
        self.minimap = self.game.map.world_map

    



    def minimap_pos(self):
        max_y = max(key[1] for key in self.minimap.keys())
        y_pos = HEIGHT - (max_y*10)
        return y_pos


    def draw(self):
        y_pos = self.minimap_pos()  # Calculate y_pos using the minimap_pos method
        for pos, value in self.minimap.items():
            x, y = pos  # Extract x and y components from the tuple
            pg.draw.rect(self.game.screen, 'white', (x * 10, (y_pos + y * 10), 10, 10), 1)
    