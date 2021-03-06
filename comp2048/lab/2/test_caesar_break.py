# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy\
 le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr \
 lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp w\
 fnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye escz\
 h te lhlj Depaspy Slhvtyr"
message="cbmm"
#message = "Iwt fjxrz qgdlc udm yjbets dktg iwt apon sdv"
#message = "Wtaad bn cpbt xh hwpzth x pb ldgzxcv pi iwt jcxktghxin du fjttchapcs stepgibtci du rdbejitg hrxtcrt"
#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    #print(letter, ":", freq)
    #INSERT CODE TO REMEMBER MAX
    if (letter != ' ' and maxFreq < freq):
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = ( ord(maxLetter) - ord('l') ) % 26 #COMPUTE SHIFT HERE
print("Predicted Shift:", shift)

from test_caesar import Caesar

c = Caesar(message, 26-shift)
c.create_keys()
c.encrypt()
print("Broken: " + c.nums_to_letters(c.encryptedMessage))
