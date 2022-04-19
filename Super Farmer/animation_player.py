import pygame
from settings import *


class AnimationPlayer:
    def __init__(self):
        self.fox_size = 128
        self.fox = self.load_spritesheet(path_fox)

    def load_spritesheet(self, path: str):
        actions = {'idle': [], 'look_around': [], 'run': []}
        sheet = pygame.image.load(path).convert_alpha()
        for index, action in enumerate(actions):
            if index == 0:
                for i in range(0, 5):
                    actions[action].append(sheet.subsurface(pygame.Rect(i * 32, 0, 32, 32)))
            elif index == 1:
                for i in range(0, 14):
                    actions[action].append(sheet.subsurface(pygame.Rect(i * 32, 32, 32, 32)))
            elif index == 2:
                for i in range(0, 8):
                    actions[action].append(sheet.subsurface(pygame.Rect(i * 32, 64, 32, 32)))

        return actions

    
    def play_animation(self, action: str, screen: pygame.Surface, x: int, y: int, index: int = 0):
        if action == 'idle':
            screen.blit(
                pygame.transform.scale(self.fox['idle'][index], (self.fox_size, self.fox_size)), 
                (x, y))
        elif action == 'look_around':
            screen.blit(
                pygame.transform.scale(self.fox['look around'][index], (self.fox_size, self.fox_size)), 
                (x + index * 10, y))
        elif action == 'run':
            screen.blit(
                pygame.transform.scale(self.fox['run'][index], (self.fox_size, self.fox_size)), 
                (x, y))

