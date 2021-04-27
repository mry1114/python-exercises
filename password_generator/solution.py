# Password generator 
# A mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. 

import string
import random

numbers = string.digits # numbers = '0123456789'
letters = string.ascii_lowercase # letters = 'abcdefghijklmnopqrstuvwxyz'
letters_upper = string.ascii_uppercase # letters_upper = letters.upper()
symbols = string.punctuation # symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

characters_lists = [numbers, letters, letters_upper, symbols]

pw_len = int(input('please enter length of password you would like to generate (minimum length is 4).\npassword length is:'))
password= []

for i in range(0, pw_len + 1):
  g = random.randint(0, 3)
  element = random.choice(characters_lists[g])
  password.append(element)
  result = ''.join(password)

print('password generated is:', result)
# Improvement to be made: the above code is unable to generate a password 
# with at leats one number, at least one lowercase letter, one uppercase letter
# and at least one symbol