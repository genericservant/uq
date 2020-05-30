

import numpy as np
from scipy import signal

class Lagton(object):
    """docstring for Lagton."""
    MAP = {\
            'N': (0, 1),\
            'E':(1, 0),\
            'S': (0, -1),\
            'W':(-1, 0)\
            }
    DIRECTIONS=['N', 'E', 'S', 'W']

    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid=np.zeros((N,N), np.uint)
        self.finite=finite
        self.fastMode=fastMode
        self.aliveValue=1
        self.deadValue=0
        self.ant_cell=(int(N/2), int(N/2))
        self.ant_direction=0

    def getStates(self):
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self):
        def mod(a, b):
            r = a % b
            if r < 0:
                r += b
            return r

        def rotate(mode):
            if mode=='C':
                self.ant_direction=mod(self.ant_direction+1, len(Lagton.DIRECTIONS))
            elif mode=='A':
                self.ant_direction=mod(self.ant_direction-1, len(Lagton.DIRECTIONS))
            move_x, move_y = Lagton.MAP[Lagton.DIRECTIONS[self.ant_direction]]
            print(move_x, move_y)
            self.ant_cell = (self.ant_cell[0]+move_x, self.ant_cell[1]+move_y)

        if self.grid[self.ant_cell[0]][self.ant_cell[1]] == 0:
            self.grid[self.ant_cell[0]][self.ant_cell[1]]=1
            rotate('C')
        elif self.grid[self.ant_cell[0]][self.ant_cell[1]] == 1:
            self.grid[self.ant_cell[0]][self.ant_cell[1]]=0
            rotate('A')

    def show(self):
        column, row = self.grid.shape
        for y in range(0, row):
            line=""
            for x in range(0, column):
                line+="{}".format(self.grid[y][x])
            print(line)
        print("ant at {} direction {}".format(self.ant_cell, Lagton.DIRECTIONS[self.ant_direction]))

if __name__=="__main__":
    life=Lagton(11)
    life.show()
    life.evolve()
    life.show()
    life.evolve()
    life.show()
    life.evolve()
    life.show()
    life.evolve()
    life.show()
    life.evolve()
    life.show()
