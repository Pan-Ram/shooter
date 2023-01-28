import pygame
import os
pygame.init()

def file_path(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path

FPS = 40
WIN_WIDTH = 700
WIN_HEIGHT = 500

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(file_path("background.png"))
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, sprite_width, sprite_height):
        super().__init__()
        self.image = pygame.image.load(file_path(sprite_image))
        self.image = pygame.transform.scale(self.image, (sprite_width, sprite_height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

play = True
game = True

background_music = pygame.mixer.music.load(file_path("music.wav"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play == True:
        window.blit(background, (0, 0))

    clock.tick(FPS)
    pygame.display.update()