class Settings():
    def __init__(self) -> None:
        #Ustawienia ekranu i tła
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #Ustawienia snake'a
        self.snake_color = (255,255,255)
        self.snake_size = 20
        self.snake_speed = 5.0
        self.snake_step = self.snake_size

        #Ustawienia jedzenia
        self.food_color = (0,0,200)

        #Ustawienia gry
        self.game_active = False





        