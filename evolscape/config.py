# -*- coding: utf-8 -*-
#Constants
VERSION = 0.1
LOG_FILE = 'log.txt'
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
WINDOW_TITLE = 'Evolscape'

# Resources
DATA_PATH = "../data/"
TILESET_PATH = DATA_PATH + "tilesets"
LEVEL_PATH = DATA_PATH + "levels"

# Time
MAX_DELTA = 0.1 # Dt can be a max of 0.1 seconds
SLOW_MOTION_RATIO = 1

# Rendering
SCALE = 1
TILE_WIDTH = 16
TILE_HEIGHT = 16
ALPHA_KEY = [255, 0, 255]

#      U  R  D   L
DX = [ 0, 1, 0, -1]
DY = [-1, 0, 1,  0]
