import pygame
from menu import Menu
from constants import *

pygame.init()

# BLACK BOX

def test_animationclose():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    exepect= menu.animation(screen)
    assert exepect == False

def test_animation():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    exepect= menu.animation(screen)
    assert exepect == True


# WHITE BOX
    
def test_initial_menustart():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    exepect = menu.initial_menu(screen)
    assert exepect == True

def test_initial_menuexit():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    exepect = menu.initial_menu(screen)
    assert exepect == False
