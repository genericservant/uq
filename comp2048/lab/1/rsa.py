# -*- coding: utf-8 -*-
"""
RSA Encryption script

Created on Fri Feb  1 12:56:03 2019

@author: shakes
"""

class RSA:
    '''
    RSA encryption class for encrypting/decrypting messages using modular exponentiation.
    '''
    def __init__(self, pubKey, key, mod):
        '''
        Constructor
        '''
        self.publicKey = pubKey #used to encrypt, everyone has access and can use
        self.privateKey = key #private, only you can use to decrypt
        self.modulus = mod

    def encrypt(self, m):
        '''
        Encrypt number given keys
        '''
        #modpow
        return m**self.publicKey % self.modulus

    def decrypt(self, c):
        '''
        Decrypt number given keys
        '''
        #modpow
        return c**self.privateKey % self.modulus

Encryptor = RSA(17, 413, 61*53)
message = 9
print("Message:", message)
encryptedMessage = Encryptor.encrypt(message)
print("Encrypted Message:", encryptedMessage)
decryptedMessage = Encryptor.decrypt(encryptedMessage)
print("Decrypted Message:", decryptedMessage)
