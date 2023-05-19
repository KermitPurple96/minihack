import random 
import string
import os
from base64 import b64encode

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

os.system("touch file")
file = ("file")


real_flag = "0fBJFv9yINChkOPMqV46Z3QRi"
b64_flag = b64encode(real_flag.encode()).decode()

for i in range(1, 401):
        
        flag_chars = random.sample(s, 25)
        flag = ''.join(flag_chars)
        f = open(file, "a")

        if i == 294:
            f.write(b64_flag + "\n")
        else:
            f.write(flag + "\n")

#solucion: cat file | awk 'NR==194' | base64 -d; echo