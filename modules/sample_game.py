import pygame
from pygame.locals import *
from datetime import datetime, timedelta

class Sun():
    def __init__(self):
        self.sun_img = pygame.image.load('assets/img/sun.png')
        self.grid_x = 0 #self.position
        self.grid_y = 0
        
        self.current_datetime = datetime.now() + timedelta(milliseconds=250)

    def asset(self):
        # x = self.grid_x * 
        # screen.blit(self.sun_img, (100, 100))
        return self.sun_img

    def move(self, x, y):
        self.grid_x = x
        self.grid_y = y

    def do_work(self):
        if datetime.now() > self.current_datetime:
            self.grid_x = self.grid_x + 1
            if self.grid_x == 16:
                self.grid_x = 0
            self.current_datetime = datetime.now() + timedelta(milliseconds=250)
        


class SampleGame1():

    def __init__(self):
        self.screen_width = 800     # Grid col 16 
        self.screen_height = 600    #      row 12
        self.tile_size = 50
        # Calculate grid
        self.max_grid_col = int(self.screen_width  / self.tile_size)
        self.max_grid_row = int(self.screen_height / self.tile_size)
        #
        self.run = True
        self.sprites = {}

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Platformer')
        self.load_assets()

        self.clock = pygame.time.Clock()
        self.clock.tick(30) # Ensure program maintains a rate of 30 frames per second

    def load_assets(self):
        #load images
        self.bg_img = pygame.image.load('assets/img/waterfall.jpg')
        self.sprites['sun'] = Sun()

    def draw_grid(self):
        for line in range(0, self.max_grid_col):
            pygame.draw.line(self.screen, (200, 200, 200), (0, line * self.tile_size), (self.screen_width, line * self.tile_size))
            pygame.draw.line(self.screen, (200, 200, 200), (line * self.tile_size, 0), (line * self.tile_size, self.screen_height))

    def redraw(self):
        """Do all drawing here"""
        self.screen.blit(self.bg_img, (0, 0))

        for sprite_id in self.sprites:
            # sprite.draw()
            sprite = self.sprites[sprite_id]
            self.screen.blit(sprite.asset(), (sprite.grid_x * self.tile_size, sprite.grid_y + self.tile_size))
        
        #world.draw()
        self.draw_grid()

    def sprites_do_work(self):
        for sprite_id in self.sprites:
            sprite = self.sprites[sprite_id]
            sprite.do_work()


    def run_game(self):

        while self.run:
            # Move
            self.sprites_do_work()

            # 
            self.redraw()
            
            # print("X" + str(datetime.now()))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            pygame.display.update()
        pygame.quit()
