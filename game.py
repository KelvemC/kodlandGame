import pgzrun
from pgzero.actor import Actor  # Adicionado para Pylance
from pgzero.builtins import music, sounds
import random
import math
from pygame import Rect

#Global configs
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.5
JUMP_STRENGTH = -12
MAX_LIVES = 3

#Initial game state
MENU = 0
PLAYING = 1
GAME_OVER = 2
VICTORY = 3
game_state = MENU

#Background Music
music.play('')

#Class

class Human(Actor):
    def __init__(self):
        super().__init__('player_idle')
        self.pos = (100, HEIGHT - 100)
        self.velocity_x = 0
        self.on_ground = False
        self.lives = MAX_LIVES
        self.animation_frame = 0
        self.animation_speed = 0.1
        self.direction = 1
        self.idle_images = ['player_idle']
        self.walk_images = ['player_walk1', 'player_walk2']
        self.jump_images = ['player_jump']

    def update_movement(self, platforms):
        self.velocity_y += GRAVITY
        self.y += self.velocity_y
        self.x += self.velocity_x

        self.on_ground = False
        if self.y >= HEIGHT - self.height / 2:
            self.y = HEIGHT - self.height /2
            self.velocity_y = 0
            self.on_ground = True
        else:
            for platform in platforms:
                if self.colliderect(platform):
                    if self.velocity_y > 0:
                        self.y = platform.top - self.height / 2
                        self.velocity_y = 0
                        self.on_ground = True
        
        self.x = max(self.width / 2, min(self.x, WIDTH - self.width / 2))
    
    def animate(self):
        self.animation_frame += self.animation_speed
        if not self.on_ground:
            self.image = self.jump_images[0]
        
        elif abs(self.velocity_x)>0:
            frame = math.floor(self.animation_frame) % len(self.walk_images)
            self.image = self.walk_images[frame]
        
        else:
            self.image = self.idle_images[0]

        if self.direction == -1:
            self.image = self.image + '_flip'
    
    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH
            sounds.jump.play()
            self.on_ground = False

class Zombie(Actor):
    def __init__(self, start_x, start_y, patrol_range):
        super().__init__('zombie_walk1')
        self.pos = (start_x, start_y)
        self.velocity_x = 2  # Velocidade inicial
        self.patrol_start = start_x - patrol_range / 2
        self.patrol_end = start_x + patrol_range / 2
        self.animation_frame = 0
        self.animation_speed = 0.08
        self.walk_images = ['zombie_walk1', 'zombie_walk2']
    
    def update_movement(self):
        self.x += self.velocity_x
        if self.x <= self.patrol_start or self.x >= self.patrol_end:
            self.velocity_x = -self.velocity_x

    def animate(self):
        self.animation_frame += self.animation_speed
        if abs(self.velocity_x) > 0:
            frame = math.floor(self.animation_frame) % len(self.walk_images)
            self.image = self.walk_images[frame]
        else:
            self.image = self.idle_images[0]