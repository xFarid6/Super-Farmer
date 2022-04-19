import pygame 
from sys import exit
from math import sin, cos, pi
from time import sleep
from spritesheet import SpriteSheet

# ???????????????????????? surface.get_shifts() # ??????????????????


pygame.init()
screen = pygame.display.set_mode((720, 640))
clock = pygame.time.Clock()

surface = pygame.Surface((300, 300))

path_backgrounds = "C:\Cose Nuove\Code\General Assets\MR-Platformer-PixelAssets-v1\Main\Backgrounds"
path_fox = "C:\Cose Nuove\Code\General Assets\Fox Sprite Sheet.png"

foxs = SpriteSheet(path_fox)
foxs_list = foxs.image_at([0, 0, 16, 16])

while True:
    screen.fill((255, 255, 255))
    surface.fill((200, 200, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                while surface.get_width() <= 600:
                    surface = pygame.transform.scale(surface, (surface.get_width() + 20, 600))
                    screen.blit(surface, (20, 20))
                    pygame.display.update(surface.get_rect())
                    sleep(0.1)


    screen.blit(surface, (20, 20))
    screen.blit(foxs_list, (20, 20))
    
    pygame.display.flip()
