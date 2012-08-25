#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os.path
import pygame
import pygame.locals as pgl

import config
from image_cache import ImageCache


class Game(object):
    LEFT_MOUSE = 1
    MIDDLE_MOUSE = 2
    RIGHT_MOUSE = 3

    def __init__(self):
        background_fill = (255, 255, 255)
        self.w, self.h = config.WINDOW_WIDTH, config.WINDOW_HEIGHT
        size = (self.w, self.h)

        self.running = False
        self.clock = pygame.time.Clock() 
        self.screen_size = size
        self.fps = 0
        self.oldTime = 0
        self.elapsedTime = 0

        # Create the window
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(background_fill)
        pygame.display.flip()

        self.image_cache = ImageCache()
        self._setup()

    def _setup(self):
        self._load_resources()
        self._load_level('test', 'test.txt')
        # Sprite container
        self.sprites = pygame.sprite.RenderUpdates()

    def _load_resources(self):
        self.image_cache.add('sprites', os.path.join(config.TILESET_PATH, 'sprites.png'))
    
    def _load_level(self, name, filename):
        pass
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pgl.QUIT:
                self.running = False
            elif event.type == pgl.KEYDOWN:
                self.key_down(event.key)
            elif event.type == pgl.KEYUP:
                if event.key == pgl.K_ESCAPE:
                    self.running = False
                self.key_up(event.key)
            elif event.type == pgl.MOUSEBUTTONDOWN:
                self.mouse_down(event.button, event.pos)
            elif event.type == pgl.MOUSEBUTTONUP:
                self.mouse_up(event.button, event.pos)
            elif event.type == pgl.MOUSEMOTION:
                self.mouse_motion(event.buttons, event.pos, event.rel)
    
    def wait_for_key(self):
        press = False
        while not press:
            for event in pygame.event.get():
                if event.type == pgl.KEYUP:
                    press = True
                    
    def key_pressed(self, key):
        keys = pygame.key.get_pressed()
        return keys[key]

    def key_down(self, key):
        pass
        
    def key_up(self, key):
        pass
    
    def mouse_down(self, button, pos):
        pass

    def mouse_up(self, button, pos):
        pass
        
    def mouse_motion(self, buttons, pos, rel):
        pass

    def check_inputs(self):
        pass
      
    def update(self, dt):
        self.check_inputs()

    def draw(self):
        # todo: create a level and return a background surface
        # self.sprites.clear(self.screen, self.background)
        pygame.display.update(self.sprites.draw(self.screen))

    def main_loop(self, fps_cap=30):
        self.running = True
        self.fps = fps_cap
        
        while self.running:
            currentTime = pygame.time.get_ticks() / 1000.0
            delta = currentTime - self.oldTime
            self.oldTime = currentTime

            # Slow-mo?
            # delta /= config.SLOW_MOTION_RATIO
            self.elapsedTime += delta

            num_iterations = int(delta / config.MAX_DELTA) + 1 
            if num_iterations != 0:
                delta /= num_iterations

            pygame.display.set_caption("FPS: %i" % self.clock.get_fps())
            self.handle_events()

            for i in xrange(num_iterations):
                self.update(delta)

            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
        

if __name__ == '__main__':
    game = Game()
    game.main_loop()
