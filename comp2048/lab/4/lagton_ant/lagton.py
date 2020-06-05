

import numpy as np

class Lagton(object):
    """docstring for Lagton."""
    MAP = {\
            'N': (-1, 0),\
            'E':(0, 1),\
            'S': (1, 0),\
            'W':(0, -1)\
            }
    DIRECTIONS=['N', 'E', 'S', 'W']

    def __init__(self, N=256):
        self.grid=np.zeros((N,N), np.uint)
        self.aliveValue=1
        self.deadValue=0
        self.ant_cell=(int(N/2), int(N/2))
        self.ant_direction=3

    def getStates(self):
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self):
        def rotate(mode):
            if mode=='C':
                self.ant_direction+=1
                if self.ant_direction >= 4:
                    self.ant_direction=0
            elif mode=='A':
                self.ant_direction-=1
                if self.ant_direction <= -4:
                    self.ant_direction=0

        def move():
            move_r, move_c = Lagton.MAP[Lagton.DIRECTIONS[self.ant_direction]]
            self.ant_cell = (self.ant_cell[0]+move_r, self.ant_cell[1]+move_c)

        def toggle(value):
            updated=np.array(self.grid)
            updated[self.ant_cell[0]][self.ant_cell[1]]= value
            return updated
        #change direction
        if self.grid[self.ant_cell[0]][self.ant_cell[1]] == self.deadValue:
            rotate('C')
            value=self.aliveValue
        elif self.grid[self.ant_cell[0]][self.ant_cell[1]] == self.aliveValue:
            rotate('A')
            value=self.deadValue
        #toggle cell
        self.grid=toggle(value)

        #move
        move()

    def show(self):
        row, column = self.grid.shape
        for c in range(0, column):
            line=""
            for r in range(0, row):
                line+="{}".format(self.grid[r][c])
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
