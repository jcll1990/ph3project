import pygame as pg
from collections import deque
from settings import *
import os


class Weapon:
    def __init__(self, game):
        self.game = game
        self.path ='resources/sprites/weapon/shotgun/'
        self.scale = .1  # Adjust the scale to make the image smaller
        self.animation_time = 90
        self.images = self.get_images(self.path)
        self.num_images = len(self.images)
        self.image = self.images[0]

        
        self.reloading = False
        self.animation_time_prev = pg.time.get_ticks()
        self.frame_counter = 0
        self.damage = 50


    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                img = pg.image.load(file_path).convert_alpha()
                images.append(img)
        return images


    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def update(self):
        self.check_animation_time()
        self.animate_shot() 

    def draw(self):
        self.game.screen.blit(self.image, (
            HALF_WIDTH - self.images[0].get_width()  // 2,
            HEIGHT - self.images[0].get_height() * self.scale  -500  # Adjust the vertical position (e.g., subtract 20 pixels)
        ))


    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True


