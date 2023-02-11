import pygame
import os
from random import randint
pygame.init()

def file_path(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path

FPS = 60
WIN_WIDTH = 700
WIN_HEIGHT = 500
GREEN = (0, 255, 0)
RED = (255, 0, 0)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(file_path("background.png"))
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed, width, height):
        super().__init__()
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image, x, y, speed, width, height):
        super().__init__(image, x, y, speed, width, height) 
    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed
        
    def fire(self):
        bullet = Bullet(file_path("bullet.png"), self.rect.centerx, self.rect.top, 5, 20, 20)
        bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self, image, x, y, speed, width, height):
        super().__init__(image, x, y, speed, width, height)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class Enemy(GameSprite):
    def __init__(self, image, x, y, speed, width, height):
        super().__init__(image, x, y, speed, width, height)
    
    def update(self):
        global missed_enemies
        self.rect.y += self.speed
        if self.rect.y >= WIN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = randint(0, WIN_WIDTH - self.rect.width)
            self.speed = randint(1, 4)
            missed_enemies += 1


player = Player("dog.png", 300, 375, 5, 65, 65)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
for i in range(5):
    enemy = Enemy(file_path("enemy.png"), randint(0, WIN_WIDTH - 50), 0, randint(1, 3), 65, 50)
    enemies.add(enemy)

killed_enemies = 0
missed_enemies = 0
font = pygame.font.SysFont("Sans Serif", 30)
font2 = pygame.font.SysFont("Sans Serif", 150)


play = True
game = True

background_music = pygame.mixer.music.load(file_path("music.wav"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    if play == True:
        window.blit(background, (0, 0))

        txt_missed = font.render("Пропущено: " + str(missed_enemies), True, RED)
        txt_killed = font.render("Збито: " + str(killed_enemies), True, GREEN)
        window.blit(txt_killed, (10, 10))
        window.blit(txt_missed, (10, 40))

        player.reset()
        player.update()

        bullets.draw(window)
        bullets.update()

        collide_bullets = pygame.sprite.groupcollide(enemies ,bullets, False, True)
        if collide_bullets:
            for enemy in collide_bullets:
                killed_enemies += 1
            
                enemy.rect.bottom = 0
                enemy.rect.x = randint(0, WIN_WIDTH - enemy.rect.width)
                enemy.speed = randint(1, 4)

        if missed_enemies >= 5 or pygame.sprite.spritecollide(player, enemies, False):
            txt_lose = font2.render("You lost", True, RED)
            window.blit(txt_lose, (150, 200))
            play = False
        if killed_enemies >= 2:
            txt_win = font2.render("You won", True, GREEN)
            window.blit(txt_win, (150, 200))
            play = False

        enemies.draw(window)
        enemies.update()


    clock.tick(FPS)
    pygame.display.update()