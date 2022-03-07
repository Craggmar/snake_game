import sys
import time
import pygame

from settings import Settings
from objects import Snake, SnakeHead, Food
from game_stats import GameStats, Scoreboard

class Snake_game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Pobranie wymiarów ekranu
        self.screen_rect = self.screen.get_rect()
        #Tytuł
        pygame.display.set_caption('Snake_game')
        #Instancje
        self.snake = []
        self.gamestats = GameStats()
        self.scoreboard = Scoreboard(self) 
        self.food = 0


    def run_game(self):        
        while True:
            #Oczekiwanie na działanie gracza
            self.check_events()
            if self.settings.game_active:           
                self.update_screen()
                self.calculate_positions()
                self.check_border_collision()
                self.check_food_collison()              
                time.sleep(0.5 / self.settings.snake_speed)
            
                           
    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    
    def calculate_positions(self):


        for snake_part in self.snake[::-1]:
            index = self.snake.index(snake_part)
            if index > 0:
                snake_part.rect.center = self.snake[index-1].rect.center
            else:
                snake_part.update_head_position()
            

    def update_screen(self):
            self.screen.fill(self.settings.bg_color)            
            self.food.draw()
            for snake_part in self.snake:
                snake_part.draw()
            self.scoreboard.show_score()            
            pygame.display.flip()

    def check_border_collision(self):
        if self.snake[0].rect.x < self.screen_rect.left or self.snake[0].rect.x >= self.screen_rect.right or \
            self.snake[0].rect.y < self.screen_rect.top or self.snake[0].rect.y >= self.screen_rect.bottom:
            self.settings.game_active = False   

    def check_food_collison(self):
        if pygame.Rect.colliderect(self.snake[0].rect, self.food.rect):
            self.food = Food(self)
            #add points
            self.gamestats.score += 1
            #add snake_part
            self.snake.append(Snake(self))
            print (len(self.snake))

    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE and self.settings.game_active ==False:
            self.snake = [SnakeHead(self)]
            self.food = Food(self)
            self.gamestats.score = 0
            self.settings.game_active = True
            self.snake[0].roll_starting_direction()
        elif event.key == pygame.K_RIGHT and self.snake[0].moving_y:
            self.snake[0].moving_x = 1
            self.snake[0].moving_y = 0
        elif event.key == pygame.K_LEFT and self.snake[0].moving_y:
            self.snake[0].moving_x = -1
            self.snake[0].moving_y = 0
        elif event.key == pygame.K_UP and self.snake[0].moving_x:
            self.snake[0].moving_x = 0
            self.snake[0].moving_y = -1
        elif event.key == pygame.K_DOWN and self.snake[0].moving_x:
            self.snake[0].moving_x = 0
            self.snake[0].moving_y = 1


if __name__=='__main__':
    sg = Snake_game()
    sg.run_game()