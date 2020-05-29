# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

#create the Turing machine
multiplier = TuringMachine(
    {
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
    ('q0', '1'): ('q1', '1', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '0'): ('q2', 'M', 'R'),
    ('q2', '1'): ('q3', '0', 'R'),
    ('q3', '1'): ('q4', '0', 'L'),
    ('q3', ''): ('qa', '', 'R'),

    ('q3', '1'): ('q4', '0', 'L'),
    ('q4', '0'): ('q4', '0', 'L'),
    ('q4', 'M'): ('q5', 'M', 'L'),
    ('q5', '1'): ('q5', '2', 'L'),
    ('q5', 'D'): ('q5', 'D', 'L'),
    ('q5', ''): ('q6', 'D', 'R'),
    ('q5', '0'): ('q5', '0', 'L'),
    ('q6', '1'): ('q6', '1', 'R'),
    ('q6', '2'): ('q7', '1', 'L'),
    ('q7', '1'): ('q7', '1', 'L'),
    ('q7', 'D'): ('q7', 'D', 'L'),
    ('q7', ''): ('q8', '1', 'R'),
    ('q8', '1'): ('q8', '1', 'R'),
    ('q8', 'D'): ('q8', 'D', 'R'),
    ('q8', '2'): ('q7', '1', 'L'),
    ('q8', 'M'): ('q9', 'M', 'R'),
    ('q9', '0'): ('q9', '0', 'R'),
    ('q9', '1'): ('q4', '0', 'L'),




    }
)
working = ['1101', '11101', '111011']
multiplier.debug('110111', step_limit=300)
'''
    COMMENTS
    x)  reduce multiplication to addition
    x)  move to sequence right of 0
    x)  if just 1 number change to X and be done with it
    x)  if more then go back and copy sequence

    y)  error double repetation everytime
    y)  can add few extra states and rectify propblem
    y)  problem is at state 5 where it changes the sequence it copied also
    y)  perhaps i should have left the original inputs incacted and made a new sequence on the left or right of it
    y)  modifications on the original input is the issue in my opinion (now that I think about it)

    x)  afterwards just have to use addition logic to get one sequence of correct multiplication

=========OUTPUT==============================================================================================

    #~ python test_turing_multiplier.py
q0                             [1]10111
q1                             1[1]0111
q1                             11[0]111
q2                             11M[1]11
q3                             11M0[1]1
q4                             11M[0]01
q4                             11[M]001
q5                             1[1]M001
q5                             [1]2M001
q5                             []22M001
q6                             D[2]2M001
q7                             [D]12M001
q7                             []D12M001
q8                             1[D]12M001
q8                             1D[1]2M001
q8                             1D1[2]M001
q7                             1D[1]1M001
q7                             1[D]11M001
q7                             [1]D11M001
q7                             []1D11M001
q8                             1[1]D11M001
q8                             11[D]11M001
q8                             11D[1]1M001
q8                             11D1[1]M001
q8                             11D11[M]001
q9                             11D11M[0]01
q9                             11D11M0[0]1
q9                             11D11M00[1]
q4                             11D11M0[0]0
q4                             11D11M[0]00
q4                             11D11[M]000
q5                             11D1[1]M000
q5                             11D[1]2M000
q5                             11[D]22M000
==========================================================ERROR copied sequence also being turned on to copy===================
q5                             1[1]D22M000
q5                             [1]2D22M000
q5                             []22D22M000
==========================================================ERROR copied sequence also being turned on to copy===================
q6                             D[2]2D22M000
q7                             [D]12D22M000
q7                             []D12D22M000
q8                             1[D]12D22M000
q8                             1D[1]2D22M000
q8                             1D1[2]D22M000
q7                             1D[1]1D22M000
q7                             1[D]11D22M000
q7                             [1]D11D22M000
q7                             []1D11D22M000
q8                             1[1]D11D22M000
q8                             11[D]11D22M000
q8                             11D[1]1D22M000
q8                             11D1[1]D22M000
q8                             11D11[D]22M000
q8                             11D11D[2]2M000
q7                             11D11[D]12M000
q7                             11D1[1]D12M000
q7                             11D[1]1D12M000
q7                             11[D]11D12M000
q7                             1[1]D11D12M000
q7                             [1]1D11D12M000
q7                             []11D11D12M000
q8                             1[1]1D11D12M000
q8                             11[1]D11D12M000
q8                             111[D]11D12M000
q8                             111D[1]1D12M000
q8                             111D1[1]D12M000
q8                             111D11[D]12M000
q8                             111D11D[1]2M000
q8                             111D11D1[2]M000
q7                             111D11D[1]1M000
q7                             111D11[D]11M000
q7                             111D1[1]D11M000
q7                             111D[1]1D11M000
q7                             111[D]11D11M000
q7                             11[1]D11D11M000
q7                             1[1]1D11D11M000
q7                             [1]11D11D11M000
q7                             []111D11D11M000
q8                             1[1]11D11D11M000
q8                             11[1]1D11D11M000
q8                             111[1]D11D11M000
q8                             1111[D]11D11M000
q8                             1111D[1]1D11M000
q8                             1111D1[1]D11M000
q8                             1111D11[D]11M000
q8                             1111D11D[1]1M000
q8                             1111D11D1[1]M000
q8                             1111D11D11[M]000
q9                             1111D11D11M[0]00
q9                             1111D11D11M0[0]0
q9                             1111D11D11M00[0]
q9                             1111D11D11M000[]
qr                             1111D11D11M000[]

'''
