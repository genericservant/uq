#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:55:41 2020

@author: toochi
"""

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,\
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')



py_dev_y = [45372, 48876, 53850, 57287, 63016,\
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='b', marker='o', label='python dev')


plt.ylabel('Median Salary (USD)')
plt.xlabel('Ages')
plt.title('Median Salary (USD) by Age')

plt.show()