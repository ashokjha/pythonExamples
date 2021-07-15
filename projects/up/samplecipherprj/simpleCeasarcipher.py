# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:45:24 2021

@author: Ashok Kumar Jha
Simple Caesar Cypher
"""

def generate_key(n=10) :
    '''
    Genarate caesar cyphar for each alphabet

    Parameters
    ----------
    n : TYPE, int
        DESCRIPTION.Shifting.  The default is 10.

    Returns
    -------
    Key Dictionary.

    '''
    uchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lchars = "abcdefghijklmnopqrstuvwxyz"
    key = {}
    cnt = 0
    for c in uchars:
        key[c] = uchars[(cnt + n) % len(uchars)]
        cnt += 1
    cnt = 0    
    for c in lchars:
        key[c] = lchars[(cnt + n) % len(lchars)]
        cnt += 1
    return key    

def encrypt(key, message):
    '''
    Encrypt the message 

    Parameters
    ----------
    key : Dict
        Dictionary of key.
    message : Str
        message to encrypt.

    Returns
    -------
    cipher : String
        Encrypted Message.

    '''
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def get_decrypt_key(key):
    '''
    Genarate decrypt dictionary

    Parameters
    ----------
    key : Dict
        Encript Dictionary

    Returns
    -------
    dkey : Dict
        Decrypt Doictionary.
    '''
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey

if __name__ == '__main__':
    key = generate_key(5)
    dkey = generate_key(21)
    cipher = encrypt(key, "YOU arE AWESOME")
    print(cipher)
    message = encrypt(dkey, cipher)
    print(message)
    dkey = get_decrypt_key(key)
    print(encrypt(dkey, cipher))
