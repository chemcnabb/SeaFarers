import pygame
class Text(pygame.sprite.Sprite):
    """ a helper class to write text on the screen """
    number = 0
    book = {}
    def __init__(self, pos, msg):
        self.number = Text.number # get a unique number
        Text.number += 1 # prepare number for next Textsprite
        Text.book[self.number] = self # store myself into the book
        pygame.sprite.Sprite.__init__(self)
        self.pos = [0.0,0.0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.msg = msg
        self.changemsg(msg)

    def update(self, seconds):
        pass

    def changemsg(self,msg):
        self.msg = msg
        self.image = write(self.msg)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

def write(msg="pygame is cool"):
    """helper function for the Text sprite"""
    myfont = pygame.font.SysFont("None", 28)
    mytext = myfont.render(msg, True, (0,0,0))
    mytext = mytext.convert_alpha()
<<<<<<< HEAD
    return mytext
=======
    return mytext
>>>>>>> 9b0d3ddde49c846ed420b3a0e450ca1ce42e6c17
