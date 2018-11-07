"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""
import network
import pygame
from functions import change_color
from random import random, uniform

class Bird:
    """
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.brain = network.Network([2,5,1])
        self.y_speed = 0
        self.skin = change_color("images/bird.png", random() + 0.5, random()+ 0.5, random()+ 0.5)
        self.alive = True
        self.score = 0
        self.nb_jumps = 0
        self.delay = 0
        self.skins = []
        self.resolution = 50
        self.init_skins(self.resolution)
    
    def init_skins(self, resolution):
        for i in range(resolution):
            self.skins.append(pygame.transform.rotate(self.skin, 90 -i*(180/resolution)))

    def copy_brain_with_mutation(self, other):
        for i in range(len(self.brain.layers)):
            for j in range(len(self.brain.layers[i].neurons)):
                for k in range(len(self.brain.layers[i].neurons[j].weights)):
                    self.brain.layers[i].neurons[j].weights[k] = other.layers[i].neurons[j].weights[k] + uniform(-0.15, 0.15)
                self.brain.layers[i].neurons[j].bias = other.layers[i].neurons[j].bias + uniform(-0.15, 0.15)

    def move(self, x_obs, y_obs):
        if self.alive:
            self.y += self.y_speed
            self.y_speed += 0.2
            self.score += 1
            self.delay -= 0.1
            
            if self.delay < 0 and self.brain.feed_forward([(x_obs - self.x) / 500, (self.y - y_obs) / 766])[0] > 0.66:
                self.y_speed = -6.5
                self.nb_jumps += 1
                self.delay = 4

        else:
            self.x -= 0.7

    def check_alive(self, ground, x_obs, ysize, space):
        if self.y >= ground:
            self.alive = False

        
        if x_obs + 130 >= self.x + 65 >= x_obs:
            if self.y + 5 < ysize or self.y + 50 > ysize + space:
                self.alive = False
                

    def __str__(self):
        return str(self.score)