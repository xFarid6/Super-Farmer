import pygame
from settings import *
import os
import time
from animation_player import AnimationPlayer
import keyboard


class SuperFarmer:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SuperFarmer")
        self.path_logo = path_assets + "logo.jpg"
        pygame.display.set_icon(pygame.image.load(self.path_logo))
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 64)
        self.clock = pygame.time.Clock()

        self.path_backgrounds = "C:\Cose Nuove\Code\General Assets\MR-Platformer-PixelAssets-v1\Main\Backgrounds"
        self.path_music = "C:\Cose Nuove\Code\General Assets\MR-Platformer-PixelAssets-v1\Main\Music"
        self.last_time = pygame.time.get_ticks()

        # bg
        self.backgrounds = self.load_backgrounds()
        self.bg_img = self.backgrounds[0]
        self.bg_img = pygame.transform.scale(self.bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg_rect = self.bg_img.get_rect()
        self.bg_buffer = self.bg_rect.copy()
        self.bg_buffer.topleft = self.bg_rect.topright

        self.plancia = pygame.image.load(path_assets + "plancia.jpg").convert_alpha()

        # animation player
        self.fox = AnimationPlayer()
        self.fox_index = 0

        # player input
        self.actions: dict = {}

        # self.starting_animation()

    def get_dt(self):
        self.current_time = pygame.time.get_ticks()
        self.dt = self.current_time - self.last_time
        self.last_time = self.current_time


    def get_input(self, actions: dict):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()


    def update(self, actions):
        self.fox_index += 0.2
        if self.fox_index >= len(self.fox.fox['run']):
            self.fox_index = 0
        self.clock.tick(FPS)

    
    def load_backgrounds(self):
        # create a list of all images in self.path_backgrounds
        backgrounds: list = []
        for image in os.listdir(self.path_backgrounds):
            # load the image
            image = pygame.image.load(os.path.join(self.path_backgrounds, image)).convert_alpha()
            backgrounds.append(image)

        return backgrounds
        

    def draw_background(self):
        self.screen.blit(self.bg_img, self.bg_rect)
        self.screen.blit(self.bg_img, self.bg_buffer)

        self.bg_rect.x -= 1
        self.bg_buffer.x = self.bg_rect.x + self.bg_rect.width

        if self.bg_rect.x <= -self.bg_rect.width:
            self.bg_rect.x = 0
            self.bg_buffer.x = self.bg_rect.x + self.bg_rect.width


    def draw(self, screen):
        self.fox.play_animation('run', screen, 
                                0, screen.get_height() - 128, 
                                int(self.fox_index))
        pygame.display.flip()


    def starting_animation(self):
        logo = pygame.image.load(self.path_logo).convert_alpha()
        logo = pygame.transform.scale(logo, (WINDOW_WIDTH, WINDOW_HEIGHT))
        logo_rect = logo.get_rect()
        self.screen.blit(logo, logo_rect)
        pygame.display.flip()
        time.sleep(0.5)
        while area_of_rect(logo_rect) > 10:
            if keyboard.is_pressed('q'):
                pygame.quit()
                exit()
            self.screen.fill((20, 20, 30, 0))
            self.screen.blit(logo, logo_rect)
            logo = pygame.image.load(self.path_logo).convert_alpha()
            logo = pygame.transform.smoothscale(logo, (logo_rect.width - 30, logo_rect.height - 5))
            logo_rect.width -= 5
            logo_rect.height -= 5
            logo_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            pygame.display.flip()
            self.clock.tick(FPS)

        
    def run(self):
        while True:
            self.get_dt()
            self.get_input(self.actions)
            self.update(self.actions)
            self.draw_background()
            self.draw(self.screen)
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = SuperFarmer()
    game.run()
