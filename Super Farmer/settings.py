import os
import pygame

WINDOW_WIDTH: int = 1000
WINDOW_HEIGHT: int = 800
FPS: int = 60

path_backgrounds: str = "C:\Cose Nuove\Code\General Assets\MR-Platformer-PixelAssets-v1\Main\Backgrounds"
path_fox: str = "C:\Cose Nuove\Code\General Assets\Fox Sprite Sheet.png"
path_assets: str = os.path.dirname(__file__) + '\\assets\\'

def area_of_rect(rect: pygame.Rect):
    return rect.width * rect.height

print(area_of_rect(pygame.Rect(0, 0, 100, 100)))