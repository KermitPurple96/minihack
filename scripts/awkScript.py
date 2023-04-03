import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

os.system("touch file")
file = ("file")

real_flag = "G7Kv31dmwTXAPfrNZVSoh6Ikl"

for i in range(1, 1001):
    
    flag_chars = random.sample(s, 25)
    flag = ''.join(flag_chars)
    f = open(file, "a")

    if i == 203:
        f.write(real_flag + " ")
    else:
        f.write(flag + " ")

#solucion: cat file | awk '{print $203}'
