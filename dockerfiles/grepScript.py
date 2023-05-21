import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

os.system("touch file1")
file = ("file1")

real_flag = "xc2IGhTCu4BLNQa0nZes3VFyl"

for i in range(0, 1000):
    
    flag_chars = random.sample(s, 25)
    flag = ''.join(flag_chars)
    f = open(file, "a")

    if i == 522:
        f.write(real_flag + "\n")
    else:
        f.write(flag + "\n")

os.system("head -n 1000 /usr/share/scripts/rockyou.txt > rock.txt")
os.system("paste rock.txt file1 > grepFile.txt")
os.system("mv grepFile.txt /home/mini1/challenge_1.txt")
os.system("rm -f file1 rock.txt")

#solucion: cat grepFile.txt | grep "disney"
