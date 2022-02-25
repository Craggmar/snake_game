import pygame.font

class GameStats():
    def __init__(self) -> None:
        self.score = 0
        self.highscore = 0

class Scoreboard():
    def __init__(self, sgame) -> None:
        self.screen = sgame.screen
        self.screen_rect = self.screen.get_rect()
        self.gamestats= sgame.gamestats
        self.settings = sgame.settings

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        self.preparate_score()

    def preparate_score(self):
        self.score_image = self.font.render(str(self.gamestats.score), True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.topright = self.screen_rect.topright 

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
            
