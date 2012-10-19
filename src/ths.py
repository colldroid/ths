#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Top Hat Surfer
# CopyLeFt 2012 Andreas Collsén
# FILENAME: ths.py

# Please note that this project is mainly
# to try out GIThub!

print 'Loading...'

import sys
sys.path.append('lib')

import main

game = main.Game()
game.startGame(game)

print 'Done!'

sys.exit(0)