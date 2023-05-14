import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

#os.system("touch /home/mini2/challenge_1.txt")
#os.system("chmod o+t /home/mini2/challenge_1.txt")
#stickybit

file = ("/home/mini2/challenge_1.txt")
real_flag = "xc2IGhTCu4BLNQa0nZes3VFyl"

for i in range(0, 1000):
    
    flag_chars = random.sample(s, 25)
    flag = ''.join(flag_chars)
    f = open(file, "a")

    if i == 522:
        f.write(real_flag + "\n")
    else:
        f.write(flag + "\n")

os.system("head -n 1000 /usr/share/scripts/rockyou.txt > /usr/share/scripts/rock.txt")
os.system("paste /usr/share/scripts/rock.txt /home/mini2/challenge_1.txt | sponge /home/mini2/challenge_1.txt")
os.system("rm -f /usr/share/scripts/rock.txt")

#solucion: cat grepFile.txt | grep "disney"
