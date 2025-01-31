import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING


DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCK =  "ducking"

#las constantes con mayus
class dinosaurio(Sprite):
    POSITION_X = 80
    POSITION_Y = 310
    POSITION_Y_DUCK = 345
    JUMP_VELOCITY = 8.5
    
    
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        
    
    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCK:
            self.duck()
            
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCK
            else:
                self.action = DINO_RUNNING
        
        if self.step >= 10:
            self.step = 0
    
    def duck(self):
       self.image = DUCKING[self.step // 5]
       self.rect = self.image.get_rect()
       self.rect.x = self.POSITION_X
       self.rect.y = self.POSITION_Y_DUCK
       self.step += 1 
       
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4 
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POSITION_Y
    
    def run(self):
        self.image = RUNNING[self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y
        self.step +=1
                                #no es obligatorio: pygame.furface
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    