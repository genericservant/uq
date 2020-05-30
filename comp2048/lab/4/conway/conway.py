# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    NMAP = [\
            (-1, -1), (0, -1), (1, -1),\
            (-1, 0), (1, 0),\
            (-1, 1), (0, 1), (1, 1),\
            ]


    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.uint)
        self.neighborhood = np.ones((3,3), np.uint) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0


    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid

    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''

        #get weighted sum of neighbors
        #PART A & E CODE HERE

        #implement the GoL rules by thresholding the weights
        #PART A CODE HERE
        self.rules(self.weighted_sum())
        #update the grid
#        self.grid = #UNCOMMENT THIS WITH YOUR UPDATED GRID

    def rules(self, nbrs):
        row, column = nbrs.shape
        for i in range(0, column):
            for j in range(0, row):
                if self.grid[i][j] == 1:
                    if nbrs[i][j] < 2 or nbrs[i][j] > 3:
                        self.grid[i][j]=0
                    elif nbrs[i][j] == 2 or nbrs[i][j] == 3:
                        self.grid[i][j]=1
                elif self.grid[i][j] == 0:
                    if nbrs[i][j] == 3:
                        self.grid[i][j]=1




    def weighted_sum(self):
        # a % b > 0
        def mod(a, b):
            r = a % b
            if r < 0:
                r += b
            return r

        row, column = self.grid.shape
        sum_grid = np.zeros((row,column), np.uint)

        for i in range(0, column):
            for j in range(0, row):
                count=0
                for cord in GameOfLife.NMAP:
                    x, y = cord
                    x = mod((i + x), column)
                    y = mod((j + y), row)
                    if self.grid[x][y] == 1:
                        count+=1
                sum_grid[i][j]=count

        return sum_grid



    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue

    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue

    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+24] = self.aliveValue

        self.grid[index[0]+1, index[1]+22] = self.aliveValue
        self.grid[index[0]+1, index[1]+24] = self.aliveValue

        self.grid[index[0]+2, index[1]+12] = self.aliveValue
        self.grid[index[0]+2, index[1]+13] = self.aliveValue
        self.grid[index[0]+2, index[1]+20] = self.aliveValue
        self.grid[index[0]+2, index[1]+21] = self.aliveValue
        self.grid[index[0]+2, index[1]+34] = self.aliveValue
        self.grid[index[0]+2, index[1]+35] = self.aliveValue

        self.grid[index[0]+3, index[1]+11] = self.aliveValue
        self.grid[index[0]+3, index[1]+15] = self.aliveValue
        self.grid[index[0]+3, index[1]+20] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+34] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue

        self.grid[index[0]+4, index[1]] = self.aliveValue
        self.grid[index[0]+4, index[1]+1] = self.aliveValue
        self.grid[index[0]+4, index[1]+10] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+20] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue

        self.grid[index[0]+5, index[1]] = self.aliveValue
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+10] = self.aliveValue
        self.grid[index[0]+5, index[1]+14] = self.aliveValue
        self.grid[index[0]+5, index[1]+16] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        self.grid[index[0]+5, index[1]+24] = self.aliveValue

        self.grid[index[0]+6, index[1]+10] = self.aliveValue
        self.grid[index[0]+6, index[1]+16] = self.aliveValue
        self.grid[index[0]+6, index[1]+24] = self.aliveValue

        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+15] = self.aliveValue

        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+13] = self.aliveValue

        #left column off by 1 and right off by 2 with starting one off by 1
    def show(self):
        row, column = self.grid.shape
        for x in range(0, row):
            line=""
            for y in range(0, column):
                line+="{}".format(self.grid[x][y])
            print(line)
    
    def insert_from_url(self, url, index=(0,0)):

        def read_url(url):
            import requests
            r=requests.get(url)
            content=r.content.decode('utf8').strip()
            stuff=[]
            j=0
            for line in content.split('\r\n'):
                if line[0] == '!':
                    j=-1
                    next
                i=0
                for ch in line:
                    if ch == "O":
                         stuff.append((j,i))
                    i+=1
                j+=1
            return stuff

        for cord in read_url(url):
            self.grid[index[0]+cord[0], index[1]+cord[1]]=self.aliveValue
