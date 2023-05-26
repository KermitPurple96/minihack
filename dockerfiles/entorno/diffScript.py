import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits

os.system("touch file1")
os.system("touch file2")
file1 = ("file1")
file2 = ("file2")

real_flag = "19cpd5mQ6mfPz5nAal28v6pxq"

for i in range(0, 50):
    
    flag_chars = random.sample(s, 25)
    flag = ''.join(flag_chars)
    f1 = open(file1, "a")
    f2 = open(file2, "a")

    if i == 39:
        f2.write(real_flag + "\n")
    else:
        f1.write(flag + "\n")
        f2.write(flag + "\n")
        
os.system("mv file1 /home/mini3/challenge_3a.txt")
os.system("mv file2 /home/mini3/challenge_3b.txt")
os.system("rm -f file1 file2")

# Solucion: diff file1 file2
