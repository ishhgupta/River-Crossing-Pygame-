import pygame as pg
import random


# DECLARING GENERAL VARIABLES
win_width = 1000
win_height = 1000
level = [0, 186, 372, 558, 744, 930]
RED = (255, 0, 0)
BLUE = (108, 221, 239)
COLOR = (255, 255, 0)
ini_x = 0
ini_y = 1000-70
end_x = 1000-70
end_y = 0


###### FUNCTION TO LOAD ALL THE IMAGES ##############################
def load_image(img_name, width, height):
    obs = pg.image.load(img_name)
    obs = pg.transform.scale(obs, (width, height))
    return obs.convert_alpha()  # remove whitespace from graphic

###### COLLISION FUNCTION #############################################


def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 < x2+w2 and x1 > x2 and y1 < y2+h2 and y1 > y2:
        return True
    if x1 < x2+w2 and x1 > x2 and y1+h1 < y2+h2 and y1+h1 > y2:
        return True
    if x1+w1 < x2+w2 and x1+w1 > x2 and y1 < y2+h2 and y1 > y2:
        return True
    if x1+w1 < x2+w2 and x1+w1 > x2 and y1+h1 < y2+h2 and y1+h1 > y2:
        return True


##### PLAYER CLASS ##########################################################
class Player:
    def __init__(self, x1, y1):
        self.collided = False
        self.x1 = x1
        self.y1 = y1
        self.vel = 9

    def update(self, keys):
        if keys[pg.K_LEFT] and self.x1 > self.vel:
            self.x1 -= self.vel
        if keys[pg.K_RIGHT] and self.x1 < win_width - 70 - self.vel:
            self.x1 += self.vel
        if keys[pg.K_UP] and self.y1 > self.vel:
            self.y1 -= self.vel
        if keys[pg.K_DOWN] and self.y1 < win_height - 70 - self.vel:
            self.y1 += self.vel

####### FIXED OBSTACLE CLASS ##################################################


class Obstacle:
    global run

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.surface = img

    def update(self, p):
        if collision(p.x1, p.y1, 70, 70, self.x, self.y, 80, 80):
            p.collided = True


####### VARIABLES USED FOR MAIN LOOP ##########################################
hold = False
loop = True
run = True
win1 = 0
win2 = 0
passed_time = 0
current_time = 0
