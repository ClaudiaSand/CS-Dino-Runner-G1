import pygame

from random import randint
from dino_runner.components.obstacles.cactus import Cactus ,SMALL_CACTUS_TYPE, LARGE_CACTUS_TYPE

class ObstacleManager:
    def __init__( self ):
        self.obstacles = []
    
    def update( self,game_speed,player,on_death ):
        if not self.obstacles:
            if randint( 0,1):
                self.obstacles.append(Cactus(SMALL_CACTUS_TYPE))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS_TYPE))
                
        for obstacle in self.obstacles:
            obstacle.update(game_speed,self.rect)
            if player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                on_death()
                
    
    def draw( self, screen ):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset( self ):
        self.obstacles = []
    
    
