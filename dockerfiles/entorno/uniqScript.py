import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

os.system("touch file")
file = ("file")
reps = [2,3,4,5,6]


real_flag = "l06Q8AmkDiLST3hfGVjNOUECM"

for i in range(0, 200):
        
        flag_chars = random.sample(s, 25)
        flag = ''.join(flag_chars)
        f = open(file, "a")

        if i == 75:
            f.write(real_flag + "\n")
        else:
            for j in range(2, 6):
                f.write(flag + "\n")

os.system("mv file /home/mini2/challenge_2.txt")
os.system("rm -f file")

#solucion: cat file | uniq -u'

