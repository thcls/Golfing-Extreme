import pygame
from constants import *
import math

class Menu:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.firt = True

    def animetion(self, screen):

        clock = pygame.time.Clock()

        index = 0
        time = 0

        space = []
        fx = []

        fx.append(pygame.image.load('fx_01.png'))
        fx.append(pygame.image.load('fx_02.png'))
        fx.append(pygame.image.load('fx_03.png'))
        fx.append(pygame.image.load('fx_04.png'))

        space.append(pygame.image.load('space1.png'))
        space.append(pygame.image.load('space2.png'))
        space.append(pygame.image.load('space3.png'))
        space.append(pygame.image.load('space4.png'))
        space.append(pygame.image.load('space5.png'))
        space.append(pygame.image.load('space6.png'))

        while True:

            clock.tick(6)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            if index == 6:
                index = 0
                time += 1
                if time == 3:
                    index = 0

                    for index in range (3):
                        clock.tick(15)
                        screen.blit(fx[index], (50, -150))
                        pygame.display.update()
                        screen.fill((0, 0, 0))

                    screen.fill((255,255,255))
                    pygame.display.update()
                    return True

            screen.blit(space[index-2], (0, 0))
            screen.blit(space[-index], (120, 100))
            screen.blit(space[index-2], (420, 200))
            screen.blit(space[-index], (620, 300))
            screen.blit(space[index-2], (700, 150))
            screen.blit(space[-index], (520, 250))
            screen.blit(space[index-2], (350, 0))
            screen.blit(space[-index], (550, 20))
            screen.blit(space[index-2], (200, 300))
            screen.blit(space[-index], (0, 300))

            pygame.display.update()
            index += 1

    def initial_menu(self, screen):

        running = self.animetion(screen)

        (x, y) = (0, 0)
        clock = pygame.time.Clock()

        ball = pygame.image.load('golf-ball8.png')
        startmenu = pygame.image.load("Initialmenu.jpg")

        screen.blit(startmenu, (0, 0))

        while running:
            clock.tick(6)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False

                if event.type == 4:
                    screen.blit(startmenu, (0, 0))
                    (x, y) = pygame.mouse.get_pos()

                if x >= 346 and y >= 224 and x <= 457 and y <= 252: #botão de start
                    screen.blit(ball, (333, 233))
                    screen.blit(ball, (459, 233))

                    if event.type == 5:
                        return True

                if x >= 362 and y >= 281 and x <= 441 and y <= 311: #botão de exit
                    screen.blit(ball, (351, 292))
                    screen.blit(ball, (443, 292))

                    if event.type == 5:
                        return False

            pygame.display.update()

    def help(self, screen):

        while True:
            text = "Utilize o mouse para escolher a direção"
            text1 = "e aperte o botão esquerdo do mouse para"
            text2 = "dar a tacada."
            text3 = "Clique para continuar..."

            window = pygame.image.load("window.png")

            screen.blit(window, (20, 20))

            font = pygame.font.SysFont(None, 30)
            help = font.render(text, True, WHITE)

            screen.blit(help, (50,50))
            help = font.render(text1, True, WHITE)
            screen.blit(help, (50, 70))

            help = font.render(text2, True, WHITE)
            screen.blit(help, (50, 90))

            help = font.render(text3, True, WHITE)
            screen.blit(help, (50, 120))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == 5:
                    return True
            pygame.display.update()
