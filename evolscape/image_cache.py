# -*- coding: utf-8 -*-
import os.path
import pygame
import config


class ImageCache(object):
    def __init__(self):
        self.cache = {}
        
    def add(self, name, filename, force_reload=False):
        if filename in self.cache and not force_reload:
            return
        return self._load(name, filename)
        
    def __getitem__(self, name):
        return self.cache.get(name)
                
    def _load(self, name, filename):
        filename = os.path.normpath(filename)
        if not os.path.exists(filename):
            raise Exception("Cannot find image %s" % filename)
        image = pygame.image.load(filename).convert()
        image.set_colorkey(config.ALPHA_KEY)
        self.cache[name] = image
        return image
