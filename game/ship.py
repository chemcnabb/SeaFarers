__author__ = 'Che'
import pygame
from pygame.locals import MOUSEBUTTONDOWN
import os
from math import sin, cos, pi, degrees, atan2

class Ship(pygame.sprite.Sprite):
    ship = pygame.image.load(os.path.join(os.getcwd(), 'game/data/images/sailboat.png'))
    angle = 90
    SPEED = 2
    speedx = 2
    speedy = 2

    def __init__(self, screen):
        self.screen = screen
        self.x = 350 #self.screen.width/2
        self.y = 250 #self.screen.height/2
        self.pos = [self.x, self.y]
        self.rect = self.ship.get_rect()
        self.sprite = pygame.transform.rotate(self.ship, self.angle)

        pygame.sprite.Sprite.__init__(self)



    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image



    def update(self):
        #rotate the car
        self.sprite = self.rot_center(self.ship, self.angle)#pygame.transform.rotate(self.ship, self.angle)
        self.rect = self.sprite.get_rect(center = self.rect.center)

        self.speedx = sin(self.angle * (pi/180))# * self.SPEED
        self.speedy = cos(self.angle * (pi/180))# * self.SPEED

        #move the car
        self.x += self.speedx
        self.y += self.speedy


        self.rect = self.sprite.get_rect()
        self.rect.center = self.x, self.y

    def get_angle(self, mousePointerCent):
        angle = atan2(-(mousePointerCent[1] - self.y), mousePointerCent[0] - self.x)
        return angle

    def events(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            mousePointerCent = pygame.mouse.get_pos()
            angle = self.get_angle(mousePointerCent)
            self.angle=degrees(angle)
