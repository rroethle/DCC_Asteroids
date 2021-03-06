import os, sys, random, math
import pygame

pygame.init()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x_axis = 1 #cosine runs paralell to the x-axis
        self.y_axis = 1 #sine runs paralell to the y-axis
        self.angle = random.randint(0, 360) #angle of rotation randomly selected 
        self.angle_of_rotation = random.randint(0,360)
        self.angluar_momentum = 4 #amount of energy the asteroid has
        self.angular_velocity = 10 #one degree of rotation per clock tick, based on frame rate
        self.image = pygame.image.load("Asteroid.gif").convert() #just the image of the asteroids
        self.radius = 30
        return

    def get_location(self):
        return (self.x_axis, self.y_axis)

    def get_angle(self):
        return self.angle_of_rotation

    def get_radius(self):
        return self.radius

    def update(self, size):
        self.x_axis += self.angluar_momentum * math.cos(math.radians(self.angle))#uses trig functions to derive the proper
        self.y_axis -= self.angluar_momentum * math.sin(math.radians(self.angle))#movement along a 2D plane for the asteroid
        self.angle_of_rotation += self.angular_velocity
        self.angle += random.randrange(-10,10)
        if self.x_axis > size[0]: #if x axis is greater than screen size then adjust the x axis
            self.x_axis = self.x_axis - size[0]
        if self.x_axis < 0:
            self.x_axis = self.x_axis + size[0]
        if self.y_axis > size[1]: #if y axis is greater than screen size then adjust the y axis
            self.y_axis = self.y_axis - size[1]
        if self.y_axis < 0:
            self.y_axis = self.y_axis + size[1]
        return

    def make_small_asteroids(self):# checks if radius is greater than 5, if it is creates two new asteroids with smaller radii
        if self.radius > 15:
            smallAsteroid = Asteroid()
            smallAsteroid.radius = 15
            smallAsteroid.x_axis = self.x_axis
            smallAsteroid.y_axis = self.y_axis
            smallAsteroid2 = Asteroid()
            smallAsteroid2.radius = 15
            smallAsteroid2.x_axis = self.x_axis
            smallAsteroid2.y_axis = self.y_axis
            return