__author__ = 'Che'
import pygame
from pygame.locals import MOUSEBUTTONDOWN
import os
from math import sin, cos, pi, degrees, atan2
from msg import Text

class Ship(pygame.sprite.Sprite):
    ship = pygame.image.load(os.path.join(os.getcwd(), 'game/data/images/sailboat.png'))
    angle = 0
    SPEED = 2
    speedx = 2
    speedy = 2
    turnDirection = 0
    turnSpeed = 50
    is_turning = True
    mouse_pos = False
    targetAngle = 90

    def __init__(self, screen):
        self.screen = screen
        screen_size = self.screen.get_size()
        self.x = screen_size[0]/2
        self.y = screen_size[1]/2
        self.pos = [self.x, self.y]
        self.rect = self.ship.get_rect()
        self.sprite = pygame.transform.rotate(self.ship, self.angle)
        self.currentAngle = self.angle
        self.targetAngle = self.currentAngle
        pygame.sprite.Sprite.__init__(self)



    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

    def rotate_ship(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        self.rect = orig_rect.copy()
        self.rect.center = rot_image.get_rect().center
        self.sprite = rot_image.subsurface(self.rect).copy()
        self.currentAngle = angle
        #return rot_image


    def set_target_angle(self):
        if self.mouse_pos:
            myRadians = atan2((self.mouse_pos[1] - self.y), (self.mouse_pos[0] - self.x))
            mydegrees = round(myRadians * 180 / pi)
            self.targetAngle = -mydegrees % 360




    def write_to_screen(self):
        statusText = Text((50, 10), r"""
        target angle: %s
        current angle: %s
        """ % (self.targetAngle, self.currentAngle))
        self.screen.blit(statusText.image, statusText.pos)

    def update(self, seconds):
        # write to screen
        self.write_to_screen()
        targetFirst = (self.targetAngle - self.currentAngle) % 360
        currentFirst = (self.currentAngle - self.targetAngle) % 360

        if self.mouse_pos:
            if targetFirst > currentFirst:
                mod = self.currentAngle - 1
                self.rotate_ship(self.ship, mod % 360)
            elif currentFirst > targetFirst:
                mod = self.currentAngle + 1
                self.rotate_ship(self.ship, mod % 360)
            if self.currentAngle == self.targetAngle:
                self.mouse_pos = False






    def events(self, event):
        if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            self.is_turning = True
            self.mouse_pos = pygame.mouse.get_pos()
            self.set_target_angle()


