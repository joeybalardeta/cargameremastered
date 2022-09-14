import pygame, sys
from pygame.locals import *
import random


#initialization
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Car Game Remastered")
music = pygame.mixer.music.load("sounds\Turquoise Cyclone.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()
pygame.mixer.music.set_pos(14.1)

#variables
scenenum = 0
streety = 0
streety2 = -800
screenset = 0
grassnum = 0
time = 0
speed = 2
hertz = 60
musicset = 0
soundset = 0

lane1 = 165
lane2 = 265
lane3 = 365
lane4 = 465
lane5 = 565
score = 0

#images and shapes
bkgd = pygame.image.load("images\Start Screen 1.png")
bkgd = pygame.transform.scale(bkgd, (960, 540))

play = pygame.image.load("images\Play Button.png")
play = pygame.transform.scale(play, (276, 90))
playrect = play.get_rect()

street = pygame.image.load("images\Road.png")
street = pygame.transform.scale(street, (800, 800))
street2 = pygame.transform.scale(street, (800, 800))

#sounds
deathsound = pygame.mixer.Sound("sounds\Death Sound.wav")



#colors
white=(255,255,255)
blue=(0,0,255)
black=(0, 0, 0)
darkgreen = (39, 102, 0)

#scorekeeper
font = pygame.font.Font('freesansbold.ttf', 32)
scoretext = font.render("Score: ", 1, white)
scoreRect = pygame.Rect(0, 0, 100, 80)



#functions/classes
class playerclass(object):
    def __init__(self, screen):
        self.screen = screen
        self.x = 365
        self.y = 675
        self.width = 70
        self.height = 40
        self.sprite = pygame.image.load("images\Car1.png")
        self.sprite = pygame.transform.scale(self.sprite, (70, 120))
        self.keyright = 0
        self.keyleft = 0

        
    def get_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def turnright(self):
        if self.x != lane5:
            self.x += 4

    def turnleft(self):
        if self.x != lane1:
            self.x -= 4
    
    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

class barrelclass(object):
    def __init__(self, screen):
        self.screen = screen
        self.y = (random.randint(1, 20)*10)-300
        self.x = (random.randint(1, 5)*100)+58
        self.width = 84
        self.height = 60
        self.sprite1 = pygame.image.load("images\Barrel1.png")
        self.sprite2 = pygame.image.load("images\Barrel2.png")
        self.sprite1 = pygame.transform.scale(self.sprite1, (84, 60))
        self.sprite2 = pygame.transform.scale(self.sprite2, (84, 60))
        self.skin = 1

    def get_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def backup(self):
        if self.y >= 810:
            self.y = (random.randint(1, 20)*10)-300
            self.x = (random.randint(1, 5)*100)+58
    def update(self):
        self.y += 4
    
    def draw(self):
        if self.skin == 1:
            self.screen.blit(self.sprite1, (self.x, self.y))
            if (time % 15 == 0):
                self.skin = 2
        if self.skin == 2:
            self.screen.blit(self.sprite2, (self.x, self.y))
            if (time % 30 == 0):
                self.skin = 1

class grass(object):
    def __init__(self, screen):
        self.list = []
        self.screen = screen
        self.sprite = pygame.image.load("images\Grass.png")
        self.grass_count = 0
        self.x = random.randint(1, 20)*5
        self.y = -10
        self.width = 10
        self.height = 10
        self.rect = Rect(0, 0, self.width, self.height)
        self.grassnum = 1

    def create(self, x, y):
        if self.grass_count < 100:
            self.grass_surface = self.rect
            self.pos = x, y
            self.list.append(self.pos)
            self.grass_count += 1
    def update(self):
        for i in range(len(self.list)):
            a, b = self.list[i]
            if b > 800:
                if self.grassnum == 0:
                    a = (random.randint(1, 13)*10)
                    self.grassnum = 1
                else:
                    a = (random.randint(67, 80)*10)
                    self.grassnum = 0

                b = (random.randint(10, 100))
                b = -b
                self.list[i] = (a, b)
            else:
                self.list[i] = (a, b+speed)

    def draw(self):
        for i in range(len(self.list)):
            self.screen.blit(self.sprite, self.list[i])

player = playerclass(screen)
grassInstance = grass(screen)
barrel = barrelclass(screen)

while True:
    clock.tick(hertz)
    mx, my = map(int, pygame.mouse.get_pos())

    if scenenum == 0:
        screen.blit(bkgd, (0,0))
        screen.blit(play, (650,435))

    if scenenum == 1:
        if musicset == 0:
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load("sounds\Old Town Road.mp3")
            if time == 60:
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(27.9)
                musicset = 1

        if screenset == 0:
            screen = pygame.display.set_mode((800, 800))
            screenset = 1
        streety += speed
        streety2 += speed
        screen.fill((0,0,0))
        screen.blit(street, (0, streety))
        screen.blit(street2, (0, streety2))
        grass(screen)
        barrelclass(screen)
        player.get_rect()
        barrel.get_rect()
        if (time % 5) == 0:
            if grassnum == 0:
                grassInstance.create(random.randint(1, 13)*10, -10)
                grassnum = 1
            else:
                grassInstance.create(random.randint(67, 80)*10, -10)
                grassnum = 0
                
        #scorekeeper
        score = (time / 30)
        score = (int(round(score)))
        scoretext = font.render("Score: ", 1, white)
        scoretext2 = font.render(str(score), 1, white)
        
        #WOOOOOOO DRAWING
        grassInstance.update()
        grassInstance.draw()
        barrel.update()
        barrel.backup()
        barrel.draw()
        player.draw()
        screen.fill(black, scoreRect)
        screen.blit(scoretext, (0, 0))
        screen.blit(scoretext2, (0, 40))
        time += 1
        if streety == 800:
            streety = -800
        if streety2 == 800:
            streety2 = -800
    
        #collision checker
        if player.rect.colliderect(barrel.rect):
            print ("E")
            scenenum = 2


    if scenenum == 2:
        pygame.mixer.music.stop()
        if soundset == 0:
            pygame.mixer.Channel(0).play(deathsound)
            soundset = 1
        endtext = font.render("Game Over!", 1, white)
        screen.fill(black)
        screen.blit(endtext, (315, 350))
    
    
    pygame.key.set_repeat(1, 10)
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        player.turnright()
    if keys[K_LEFT]:
        player.turnleft()
        
    for event in pygame.event.get():
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if event.type == MOUSEBUTTONDOWN:
            if 650<mx<926 and 435<my<525:
                scenenum = 1
                
        if event.type == QUIT:
             pygame.quit()
             sys.exit()
    pygame.event.pump()
    pygame.display.flip()
