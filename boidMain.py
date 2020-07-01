
#Eugene Liu
#9/18/2017

"""
SECTION 1:==================================================================
This part of your program is in charge of setting up the screen for the game
============================================================================
"""
#Imports for pygame
import pygame, sys, math, boid
#Initialize PyGame
pygame.init()

#Screen Setup
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Boids")

#manage how fast the screen updates 
clock = pygame.time.Clock()

"""
SECTION 2:=================================================================
This part of your program is for making objects and variables to use in your
game. This includes score, background images, characters, etc
===========================================================================
"""
#Create variables
quit = False

#Groups to hold all sprites
boidGroup = pygame.sprite.Group()

"""
============================= Game Loop ================================
"""
while not quit:
    clock.tick(30)

    # All events (mouse and keyboard)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            boidGroup.add(boid.Boid("boid.png", pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

    #Clear the screen
    screen.fill((255,255,255))

    #update sprites
    for eachBoid in range(len(boidGroup.sprites())):
        list = boidGroup.sprites()
        list.pop(eachBoid)
        boidGroup.sprites()[eachBoid].update(screen, list)

    #Draw sprites
    boidGroup.draw(screen)

    #Display the next screen
    pygame.display.flip()

#Close the window and quit.
pygame.display.quit()
sys.exit()
pygame.quit()