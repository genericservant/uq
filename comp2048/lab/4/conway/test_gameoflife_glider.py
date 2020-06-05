# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

N = 1024

#create the game of life object
life = conway.GameOfLife(N, False, True)
#life.insertBlinker((0,0))
#life.insertGlider((55,55))
#life.insertGliderGun(((0, 0)))

#life.insert_from_url("http://www.conwaylife.com/patterns/72p6h2v0.cells", index=(int(N/2),int(N/2)))



#n 123
#life.insert_from_url("http://www.conwaylife.com/patterns/gliderproducingswitchengine.cells")

#n 160
#life.insert_from_url("http://www.conwaylife.com/patterns/160p10h2v0.cells")

#n 350
#life.insert_from_url("http://www.conwaylife.com/patterns/doublex.cells")

#n 3685
#life.insert_from_url("http://www.conwaylife.com/patterns/3enginecordershiprake.cells", index=(50,50))

#n 1812
life.insert_from_url("http://www.conwaylife.com/patterns/3enginecordershipgun.cells", index=(50,50))

#size 36  n 36
'''
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(0,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(100,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(200,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(300,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(400,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(500,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(600,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(700,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(800,0))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(900,0))


life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(0,100))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(100,200))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(200,300))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(300,400))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(400,500))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(500,600))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(600,700))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(700,800))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(800,900))

life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(0,50))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(50,150))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(100,250))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(150,350))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(250,450))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(350,550))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(400,650))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(450,750))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(500,850))


life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(50,50))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(100,100))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(150,150))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(250,200))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(350,250))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(400,300))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(450,350))
life.insert_from_url("http://www.conwaylife.com/patterns/gosperglidergun.cells", index=(500,400))
'''


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
    life.show()
    cellsUpdated = life.getStates()

    img.set_array(cellsUpdated)

    return img,

interval = 200 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
