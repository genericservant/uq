# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)
# try this one, its creeping me out its like a false positive but its so weird
ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik \
							parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sg\
							fvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojf\
							o rl rylm isn aueuom! Gdwm Qopjmw!"

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"

crib = "Hail Shakes!"
crib_substring = ""
print(crib_substring)

##Break the code via brute force search
#INSERT CODE HERE
#INSERT CODE HERE
MAX_KEY_SIZE = 26
ALPHA_ASCII_START = 65
MAX_TRIALS = (MAX_KEY_SIZE)*(MAX_KEY_SIZE)*(MAX_KEY_SIZE)

# Generate Key
def keys_gen(prev_keys):
	prev_keys[0] = ( prev_keys[0] + 1 ) % MAX_KEY_SIZE
	if prev_keys[0] == 0:
		prev_keys[1] = ( prev_keys[1] + 1 ) % MAX_KEY_SIZE
		if prev_keys[1] == 0:
			prev_keys[2] = ( prev_keys[2] + 1 ) % MAX_KEY_SIZE
			if prev_keys[2] == 0:
				pass

	return prev_keys

def convert_keys(keys_n):
	keys_l = ""
	for k in keys_n:
		keys_l += chr(k+ALPHA_ASCII_START)
	return keys_l

def brute_force(keys_n):
	trial = 0
	while trial < MAX_TRIALS:
		keys_n = keys_gen(keys_n)
		print("Trial #{} Key: {}".format(trial, convert_keys(keys_n)))
		print("Starting engine with generated keys...")
		# Start engine with generated key
		engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
		rotor.ROTOR_II, rotor.ROTOR_III, key=convert_keys(keys_n),
		plugs="AA BB CC DD EE")
		print("Matching pattern...")
		decoded_ShakesHorribleMessage = engine.encipher(ShakesHorribleMessage)
		crib_substring = decoded_ShakesHorribleMessage[-12:]
		# Search match for crib at end
		if crib_substring == crib:
			print("trial #{} MATCH FOUND!!! Key = {}".format(trial, convert_keys(keys_n)))
			#Print the Decoded message
			print("Encrypted--------")
			print(ShakesHorribleMessage)
			print("Decrypted--------")
			print(decoded_ShakesHorribleMessage)
			return keys_n
		trial+=1
	return None

keys_n = [MAX_KEY_SIZE-1, MAX_KEY_SIZE-1, MAX_KEY_SIZE-1]

brute_force(keys_n)

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
	plugboard with 6 wires, paires of 6 letters being scrambled or obscured 26! / ( ( 26 - 12 )! * 2^6 * 6! )
	26^5 + [ 26! / ( ( 26 - 12 )! * 2^6 * 6! ) ] = 6704667476 -> x
	-----------
	x = 10681081 seconds ~= 123.6 days?


'''
