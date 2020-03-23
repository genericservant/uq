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
''' uncomment this to see the cracked code of the tese_caesar_break.py
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


'''
d)
	Output for time
	2012
	- 8 core i7 at 1.734GHz
	- memory 7897MiB 64bit int
	time::
		real	0m28.205s
		user	0m27.856s
		sys		0m0.166s

	1936 - The Z1 (First programmable computer)
	- Clock Speed : 1Hz
	- memory 64 words
	time::
		real	1 / ( 8 * 1.7345 * (10^6) ) ---> 28sec
				1 / ( 1 )					---> x
				---------------------------------
				x = 388527999sec ~= 12.3 years?
--
e)
	26^3 possibilities -> 28 seconds
	plugboard with 6 wires, paires of 6 letters being scrambled or obscured 26! / ( ( 26 - 11 )! * 2^6 * 6! )
	26^5 + 26! / ( ( 26 - 11 )! * 2^6 * 6! ) = 6704667476 -> x
	-----------
	x = 10681081 seconds ~= 123.6 days?


'''
