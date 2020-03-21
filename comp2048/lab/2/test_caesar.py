# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog" #type your message here
'''
message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy\
 le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr \
 lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp w\
 fnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye escz\
 h te lhlj Depaspy Slhvtyr"
'''
print("Message:", message)

#create the Caesar cypher
#offset = 5 #choose your shift
offset = -11
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        #INSERT CODE HERE
        keys[letter] = str((index+offset) % totalLetters)
    else: #uppercase
        #INSERT CODE HERE
        keys[letter] = str(totalLetters + ((index+offset-totalLetters) % (totalLetters)))

    invkeys[keys[letter]] = letter
    
print("Cypher Dict:", keys)

#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list inot string
eM = ""
for letter in encryptedMessage:
    if (letter != ' '):
        eM = eM + letters[int(letter)]
    else:
        eM = eM + letter
print(eM)
#decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string
