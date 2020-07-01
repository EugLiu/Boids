#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      s-euliu
#
# Created:     20/09/2017
# Copyright:   (c) s-euliu 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame, math, random, vector

class Boid(pygame.sprite.Sprite):
    def __init__(self, image, x = 0, y = 0):
        pygame.sprite.Sprite.__init__(self)

        #Load image
        self.standardImage = pygame.image.load(image).convert()
        self.image = self.standardImage
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        #Constants
        self.range = 75
        self.speed = 7

        #Set location on screen
        self.rect.x = x
        self.rect.y = y
        self.pos = vector.Vector(x, y)
        self.dir = vector.Vector()
        self.dir.setPolar(random.random() * 2 * math.pi, self.speed)


    def update(self, screen, others):
        if len(others) > 0:
            center = vector.Vector().add(self.pos)
            alignment = vector.Vector()
            avoidanceSum = vector.Vector()
            othersInRange = 0

            for other in others:                
                toOther = other.pos.subtract(self.pos)
                angleToOther = vector.angleBetween(self.dir, toOther)

                if toOther.mag < self.range and angleToOther < 3 / 4 * math.pi:
                    center = center.add(other.pos)
                    alignment = alignment.add(other.dir)
                    avoidanceSum = avoidanceSum.subtract(toOther.toUnitVector().scalarMultiply(50 / max(toOther.mag, 1.0) * math.cos(angleToOther * 2 / 3)))
                    othersInRange += 1

            center = center.scalarDivide(othersInRange + 1).subtract(self.pos).scalarDivide(10)
            alignment = alignment.scalarDivide(max(othersInRange, 1) * 2)
            avoidanceSum = avoidanceSum.add(center).add(alignment)
            
            # rotation limiter
            if vector.angleBetween(self.dir, self.dir.add(avoidanceSum)) > math.pi / 8:
                if self.dir.isLeftOf(self.dir.add(avoidanceSum)):
                    self.dir.setAngle(self.dir.angle + math.pi / 8)

                else:
                    self.dir.setAngle(self.dir.angle - math.pi / 8)
            else:
                self.dir = self.dir.add(avoidanceSum).toUnitVector().scalarMultiply(self.speed)
        
        # Move
        self.pos = self.pos.add(self.dir)
        if self.pos.x < 0:
            self.pos.setX(screen.get_width())
        
        elif screen.get_width() < self.pos.x:
            self.pos.setX(0)

        if self.pos.y < 0:
            self.pos.setY(screen.get_height())
        
        elif screen.get_height() < self.pos.y:
            self.pos.setY(0)
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.image = pygame.transform.rotate(self.standardImage, self.dir.angle / (math.pi * 2) * -360)