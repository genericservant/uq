# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""

#import lagton

import lagton_colors as lagton

N = 64

#create the game of life object
life = lagton.Lagton(N)
life.evolve()
cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life

    life.evolve()
    cellsUpdated = life.getStates()

    img.set_array(cellsUpdated)

    return img,

interval = 1 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
