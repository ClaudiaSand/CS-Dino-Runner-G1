import random
import pygame


from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import SmallCactus
from dino_runner.components.obstacles.obstacle import Obstacle

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacle_groups = [
            (SmallCactus(), 0.6), # 60% probability of small cactus
            (Bird(), 0.2), # 20% probability of bird
            (SmallCactus(), 0.3), # 30% probability of small cactus
        ]
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_timer = 0
        
    def update(self, game_speed, player, game):
        self.obstacle_timer += game_speed / 100.0 # increment timer based on game speed
        
        if not self.obstacles or self.obstacle_timer >= 3:
            self.obstacles = []
            self.obstacle_group.empty()
            for obstacle, probability in self.obstacle_groups:
                num_obstacles = int(probability * 4)
                for _ in range(num_obstacles):
                    self.obstacles.append(obstacle)
                    self.obstacle_group.add(obstacle)
            
            self.obstacle_timer = 0 # reset timer
        
        for obstacle in self.obstacles:
            obstacle.update(game_speed)
            if player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
        
    def draw(self, screen):
        self.obstacle_group.draw(screen)
