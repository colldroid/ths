# -*- coding: utf-8 -*-

# Top Hat Surfer
# CopyLeFt 2012 Andreas Collsén
# FILENAME: lib/main.py

import pygame
import settings
import events
import scr

class Game(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Top Hat Surfer')
        self.Settings = settings.Settings()
        self.Events = events.Listener()
        self.Screen = scr.Screen() 
    def startGame(self, gobj):
        pygame.display.set_mode(self.Settings.resolution)
        self.Events.listen(gobj)
    