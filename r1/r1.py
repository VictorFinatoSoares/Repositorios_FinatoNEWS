import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Repositório 1')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_correndo = []
        self.sprites_correndo.append(pygame.image.load('run/0.png'))
        self.sprites_correndo.append(pygame.image.load('run/1.png'))
        self.sprites_correndo.append(pygame.image.load('run/2.png'))
        self.sprites_correndo.append(pygame.image.load('run/3.png'))
        self.sprites_correndo.append(pygame.image.load('run/4.png'))
        self.sprites_correndo.append(pygame.image.load('run/5.png'))
        self.sprites_correndo.append(pygame.image.load('run/6.png'))
        self.sprites_correndo.append(pygame.image.load('run/7.png'))

        self.sprites_pulo = []
        self.sprites_pulo.append(pygame.image.load('jump/0.png'))
        

        self.atual = 0
        self.image = self.sprites_correndo[self.atual]
        self.image = pygame.transform.scale(self.image, (40, 50))

        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 100
        self.rect.topleft = self.x, self.y

        self.pulando = False
        self.velocidade_pulo = 0
        self.gravidade = 0.5

    def update(self):
        if self.pulando:
            self.atual += 0.1
            if self.atual >= len(self.sprites_pulo):
                self.atual = 0
            self.image = self.sprites_pulo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (40, 50))
            self.velocidade_pulo += self.gravidade
            self.y += self.velocidade_pulo
            if self.y >= 100:
                self.y = 100
                self.pulando = False
        else:
            self.atual += 0.5
            if self.atual >= len(self.sprites_correndo):
                self.atual = 0
            self.image = self.sprites_correndo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (40, 50))
            self.x += 5
            if self.x > 640:
                self.x = 0

        self.rect.topleft = self.x, self.y
        self.image.set_colorkey((0,0,0))

    def pular(self):
        if not self.pulando:
            self.pulando = True
            self.velocidade_pulo = -10

todas_as_sprites = pygame.sprite.Group()
player = Player()
todas_as_sprites.add(player)

relogio = pygame.time.Clock()

bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (640,479+1))

while True:

    relogio.tick(30)
    tela.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.pular()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
