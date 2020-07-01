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
import pygame, math, random

# Takes a vector and returns its calculated coords
def coordOf(a):
    return [math.cos(a.angle) * a.mag, math.sin(a.angle) * a.mag, 0]

# Takes a 2D vector and returns its calculated absolute angle [0, 2 pi)
def angleOf(a):
    if (a.x == 0): #avoiding division by 0 exception
        if (a.y < 0):
            return math.pi * 3 / 2
        else:
            return math.pi / 2

    angle = math.atan(a.y / a.x)
    if a.x < 0:
        angle += math.pi

    return angle % (2 * math.pi)

# Takes a vector and returns its calculated length
def magOf(a):
    return math.sqrt(a.x ** 2 + a.y ** 2 + a.z ** 2)



# OPERATION FUNCTIONS:
#def add(a, b):
#    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)

#def subtract(a, b):
#    return Vector(a.x - b.x, a.y - b.y, a.z - b.z)

## Takes 2 vectors and returns a vector representing the cross product
#def crossProduct(a, b):
#    return Vector(a.y * b.z - a.z * b.y, -1 * (a.x * b.z - a.z * b.x), a.x * b.y - a.y * b.x)



# UTILITY FUNCTIONS:
# Takes 2 vectors and returns the smallest angle between them (radians)
def angleBetween(a, b):
    return math.asin(a.cross(b).mag / a.mag / b.mag)



class Vector(object):
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.angle = 0.0
        self.mag = 0.0
        self.setCoord(x, y, z)

    def setX(self, x):
        self.setCoord(x, self.y, self.z)

    def setY(self, y):
        self.setCoord(self.x, y, self.z)

    def setZ(self, z):
        self.setCoord(self.x, self.y, z)

    def setCoord(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angleOf(self)
        self.mag = magOf(self)

    def setMag(self, mag):
        self.setPolar(self.angle, mag)

    def setAngle(self, angle):
        self.setPolar(angle, self.mag)

    def setPolar(self, angle, mag):
        self.angle = angle
        self.mag = mag
        coord = coordOf(self)
        self.x = coord[0]
        self.y = coord[1]
        self.z = coord[2]



    # OPERATION FUNCTIONS:
    # Takes a scalar, and performs scalar multiplication on this vector
    def scalarMultiply(self, scalar):
        #self.setCoord(self.x * scalar, self.y * scalar, self.z * scalar)
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def scalarDivide(self, scalar):
        return self.scalarMultiply(1 / scalar)

    def add(self, a):
        #self.setCoord(self.x + a.x, self.y + a.y, self.z + a.z)
        return Vector(self.x + a.x, self.y + a.y, self.z + a.z)

    def subtract(self, a):
        #self.setCoord(self.x - a.x, self.y - a.y, self.z - a.z)
        return Vector(self.x - a.x, self.y - a.y, self.z - a.z)

    def cross(self, a):
        return Vector(self.y * a.z - self.z * a.y, -1 * (self.x * a.z - self.z * a.x), self.x * a.y - self.y * a.x)

    def toUnitVector(self):
        return self.scalarDivide(self.mag)

    def isLeftOf(self, other):
        return self.cross(other).mag < 0


