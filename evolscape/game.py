#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os.path
import pygame
from pygame.locals import *

import config
from event import Event
from screen import *
from image_cache import ImageCache


class Game(Event):
    LEFT_MOUSE = 1
    MIDDLE_MOUSE = 2
    RIGHT_MOUSE = 3

    def __init__(self):
        background_fill = (0, 0, 0)
        self.w, self.h = config.WINDOW_WIDTH, config.WINDOW_HEIGHT
        size = (self.w, self.h)

        self.running = False
        self.clock = pygame.time.Clock() 
        self.screen_size = size
        self.slowmo = False

        # Create the window
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.window.fill(background_fill)
        pygame.display.flip()

        self.image_cache = ImageCache()
        self._setup()

    def _setup(self):
        self._load_resources()
        # Sprite container
        self.sprites = pygame.sprite.RenderUpdates()
        self.set_screen(GameScreen(self))

    def _load_resources(self):
        self.image_cache.add('sprites', os.path.join(config.TILESET_PATH, 'sprites.png'))

    def check_inputs(self):
        """Go through the event queue and fire off callbacks based on the inputs"""
        for event in pygame.event.get():
            self.handle_event(event)

    def set_screen(self, screen):
        if hasattr(self, 'screen'):
            self.screen.hide()
        self.screen = screen
        self.screen.show()

    def update(self, dt):
        self.screen.update(dt)

    def draw(self, dt):
        self.sprites.clear(self.window, self.screen.get_background()) 
        self.screen.draw(dt)
        pygame.display.update(self.sprites.draw(self.window))

    def main_loop(self):
        self.running = True
        self.playtime = 0
        max_fps = 60
        accum_dt = 0

        while self.running:
            dt = min(self.clock.tick_busy_loop(max_fps) * 0.001, 0.1)  
            
            seconds = pygame.time.get_ticks() / 1000.0
            self.playtime = seconds

            pygame.display.set_caption("FPS: %.2f" % self.clock.get_fps())
    
            self.check_inputs()

            if self.slowmo:
                dt /= 3

            accum_dt += dt
            while accum_dt > 0:
                dt = 0.01
                accum_dt -= dt
                self.update(dt)

            self.draw(dt)
            pygame.display.flip()

    # Events
    def on_exit(self):
        self.running = False

    def on_key_up(self, event):
        if event.key == K_ESCAPE:
            self.on_exit()

    def on_key_down(self, event):
        key = event.key

        if key == K_s:
            self.slowmo = True
        else:
            self.slowmo = False
         
    def on_mouse_lbtn_down(self, event):
        pos = event.pos

    def on_mouse_rbtn_up(self, event):
        pos = event.pos
        
    def on_mouse_motion(self, event):
        buttons, pos, rel = event.buttons, event.pos, event.rel


if __name__ == '__main__':
    game = Game()
    game.main_loop()
