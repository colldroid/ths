# -*- coding: utf-8 -*-

# Top Hat Surfer
# CopyLeFt 2012 Andreas Collsén
# FILENAME: lib/events.py

import pygame

class Listener(object):
    def __init__(self):
        self.Enabled = True
    def listen(self, gobj):
        while self.Enabled:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.Enabled = False
                    pygame.quit()
            
            #Update the screen
            gobj.Screen.update()