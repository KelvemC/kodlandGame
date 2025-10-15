import pgzero
import random
import math
from pygame import Rect

#Global configs
WIDTH = 800
HEIGHT = 600
JUMP_STRENGTH = 0.5
MAX_LIVES = 3

#Initial game state
MENU = 0
PLAYING = 1
GAME_OVER = 2
VICTORY = 3
game_state = MENU

#Background Music
music.play('')