# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
class Caesar(object):
	"""docstring for Caesar."""

	def __init__(self, message, offset):
		self.message = message
		#offset = 5 #choose your shift
		self.offset = offset
		self.totalLetters = 26
		self.keys = {} #use dictionary for letter mapping
		self.invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
		import string
		self.letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.encryptedMessage = []
		self.decryptedMessage = []
		print("Message:", self.message)

	def create_keys(self):
	#create the Caesar cypher
		for index, letter in enumerate(self.letters):
		    # cypher setup
		    if index < self.totalLetters: #lowercase
		        #INSERT CODE HERE
		        self.keys[letter] = str((index+self.offset) % self.totalLetters)
		    else: #uppercase
		        #INSERT CODE HERE
		        self.keys[letter] = str(self.totalLetters + ((index+self.offset-self.totalLetters) % (self.totalLetters)))

		    self.invkeys[self.keys[letter]] = letter

	def encrypt(self):
		#encrypt
		for letter in self.message:
		    if letter == ' ': #spaces
		        self.encryptedMessage.append(letter)
		    else:
		        self.encryptedMessage.append(self.keys[letter])

	def decrypt(self):
		#decrypt
		for letter in self.encryptedMessage:
		    if letter == ' ': #spaces
		        self.decryptedMessage.append(letter)
		    else:
		        self.decryptedMessage.append(self.invkeys[letter])

	def nums_to_letters(self, m):
		eM = ""
		for letter in m:
		    if (letter != ' '):
		        eM = eM + self.letters[int(letter)]
		    else:
		        eM = eM + letter
		return eM




DEFAULT_MESSAGE = "The quick brown fox jumped over the lazy dog" #type your message here
''' uncomment this to see the cracked code of the tese_caesar_break.py
message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy\
le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr \
lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp w\
fnvj p	yzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye escz\
h te lhlj Depaspy Slhvtyr"
'''
DEFAULT_MESSAGE="ball"
DEFAULT_OFFSET = +1

def get_argument():
	import sys
	if (len(sys.argv) == 1):
		print("python test_caesar.py \"string to encrypt\" offset")
		print("--- Currently running default script ---")
		return DEFAULT_MESSAGE, DEFAULT_OFFSET
	elif (len(sys.argv) == 2):
		return DEFAULT_MESSAGE, int(sys.argv[1])
	elif (len(sys.argv) == 3):
		return sys.argv[1], int(sys.argv[2])
	else:
		return " ".join(sys.argv[1:-2]), int(sys.argv[-1])

if __name__ == "__main__":
	message, offset = get_argument()
	c = Caesar(message, offset)
	c.create_keys()
	print("Cypher Dict:", c.keys)
	c.encrypt()
	print("Encrypted Message:", ''.join(c.encryptedMessage)) #join is used to put list inot string
	print(c.nums_to_letters(c.encryptedMessage))
	c.decrypt()
	print("Decrypted Message:", ''.join(c.decryptedMessage)) #join is used to put list inot string
