import pygame
from menu import Menu
from constants import *

pygame.init()

# BLACK BOX

def test_animationclose():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect= menu.animation(screen)
    assert expect == False
    
def test_animation():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect= menu.animation(screen)
    assert expect == True

# BLACK BOX

def test_initial_menustart():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect = menu.initial_menu(screen)
    assert expect == True

def test_initial_menuexit():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect = menu.initial_menu(screen)
    assert expect == False
