# -*- coding: cp1252 -*-
# Fabien Toune
# encrypt.py
# Oct 17, 2012
import string

phrase = raw_input("Enter sentence to encrypt: ")
shift = input("Enter shift value: ")
encoded_phrase = ''
for c in phrase:
    if c.isalpha():
        code = ord(c)
        if code < 91:   #lowercase
            base = 65
        else:           #uppercase
            base = 97
        code -= base
        code += shift
        code = code%26
        code += base
        c = chr(code)
    encoded_phrase += c
print "The encoded phrase is:", encoded_phrase
        
            
        
