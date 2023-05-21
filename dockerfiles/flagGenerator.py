import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

flag_chars = random.sample(s, 25)
flag = ''.join(flag_chars)
print(flag)
