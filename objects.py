import pygame
from random import randint, choice


class Snake():
    def __init__(self, sgame) -> None:
        '''Inicjalizacja i położenie poczatkowe'''
        self.settings = sgame.settings
        self.color = self.settings.snake_color
        self.screen = sgame.screen
        self.screen_rect = sgame.screen.get_rect()

        self.rect = pygame.Rect(0,0, self.settings.snake_size, self.settings.snake_size)
        self.rect.topleft = tuple(map(lambda x, y: x + y, self.screen_rect.center, (-self.settings.snake_size,-self.settings.snake_size)))

        self.moving_x = 0
        self.moving_y = 0       
    
    def draw(self):
        '''Wyświetlenie snake'a'''
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.snake_size/2)

    def roll_starting_direction(self):
        self.moving_x = choice((-1,0,0,1))
        if self.moving_x == 0:
            self.moving_y = choice((-1,1))

    def update_position(self):
        '''Akutalizacja pozycji'''
        self.rect.x += self.settings.snake_step * self.moving_x
        self.rect.y += self.settings.snake_step * self.moving_y



class Food():
    def __init__(self, sgame) -> None:
        self.settings = sgame.settings
        self.color = self.settings.food_color
        self.screen = sgame.screen
        self.screen_rect = sgame.screen.get_rect()

        self.rect = pygame.Rect(0,0, self.settings.snake_size, self.settings.snake_size)
        self.rect.x = randint (0, (self.settings.screen_width - self.settings.snake_size)/self.settings.snake_size)*self.settings.snake_size
        self.rect.y = randint (0, (self.settings.screen_height - self.settings.snake_size)/self.settings.snake_size)*self.settings.snake_size


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    

