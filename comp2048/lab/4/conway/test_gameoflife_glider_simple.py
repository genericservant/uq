# -*- coding: utf-8 -*-
"""
Game of life simple script for checking init states and checking if the evolution is
implemented correctly.

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 64

#create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((0,0))
#life.insertGlider((30,30))
#life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells")
cells = life.getStates() #initial state

#evolve once
life.evolve()
cellsUpdated1 = life.getStates()

#evolve twice
life.evolve()
cellsUpdated2 = life.getStates()
for i in range(0, 64):
    st=""
    for j in range(0, 64):
        st+=str(cellsUpdated1[i][j])
    print(st)
print("---------xxxxxxxxx---------")
for i in range(0, 64):
    st=""
    for j in range(0, 64):
        st+=str(cellsUpdated2[i][j])
    print(st)
#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import numpy as np

plt.figure(0)
plt.gray()
plt.imshow(cells)

ax = plt.gca()
# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
#grid
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.figure(1)
plt.imshow(cellsUpdated1)
#
plt.figure(2)
plt.imshow(cellsUpdated2)

plt.show()
