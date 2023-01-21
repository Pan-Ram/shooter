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