# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 64

#create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((60,15))
#life.insertGlider((55,55))
#life.insertGliderGun(((0, 0)))
life.insert_from_url("http://www.conwaylife.com/patterns/258p3onachimsp11.cells")
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

interval = 200 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
