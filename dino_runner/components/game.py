#from typing import self
import pygame
from dino_runner.components.dinosaurio import dinosaurio
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DINO_START, FONT_STYLE, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.obstacles.obstacle_manager  import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.achievement = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        #dias 1 viernes
        self.player = dinosaurio()
        #dia 2 lunes
        self.obstaclemanager= ObstacleManager()
        self.death_count = 0
        self.score = Score()
    
    def run( self):
        self.achievement = True
        while self.achievement:
            if not self.playing:
                self.show_menu()
        
        pygame.quit()
        
    def start_game(self):
        # Game loop: events - update - draw
        self.playing = True
        #self.obstaclemanager.reset() ## arreglar me cierra el juego al jugarlo
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input) 
        self.obstaclemanager.update(self.game_speed,self.player,self, self.on_death)
        self.score.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstaclemanager.draw(self.screen)
        self.score.draw(self.screen)
        # pygame.display.update()6
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        self.playing = False
        self.death_count += 1
        

    def show_menu (self):
        # rellenar de color blanco
        self.screen.fill((255,255,255))
        # mensaje de bienvenida central
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            font = pygame.font.Font( FONT_STYLE, 32)
            text = font.render(
                " WELCOME!, Press any key to start the game", True, (5,5,5))
            text_rect = text.get_rect() 
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        else:
            self.screen.blit(GAME_OVER, (half_screen_width -
                         220, half_screen_height - 5))
            pass
        # poner una imagen de modo de icono
        self.screen.blit(DINO_START, (half_screen_width -
                         80, half_screen_height - 120))
        # Plasmar los cambios
        pygame.display.update()
        # Manejar eventos 
        self.handle_menu_events()
    
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                self.playing = False
                self.achievement = False
                
            elif event.type == pygame.KEYDOWN:
                self.start_game()
        
        
        
        