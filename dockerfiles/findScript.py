import random 
import string
import os

s = string.ascii_lowercase + string.ascii_uppercase + string.digits
fake_perms = [1,4,5]

for j in range(0, 9):
    os.system("mkdir directory%s" % j)
    for i in range(0, 50):
        os.system("touch directory%s/file%s" % (j, i))
        file = ("directory%s/file%s" % (j, i))
        p1 = random.randrange(0,7)
        p2 = random.randrange(0,7)
        p3 = random.choice(fake_perms)
        os.system("chmod %d%d%d directory%s/file%s" % (p1, p2, p3, j, i))
        os.system("chown root:kermit directory%s/file%s" % (j, i))
        chars = random.randrange(10,25)
        flag_chars = random.sample(s, chars)
        flag = ''.join(flag_chars)
        f = open(file, "a")
        f.write(flag)

real_flag = "copekLgQ6m1Pz5nAHrXuEG"
os.system("echo %s > directory4/file16" % (real_flag))
os.system("chmod o+w directory4/file16")


#hay que asignar todos los archivos como pertenecientes al usuario siguiente nivel
#para que el que se debe encontrar es el unico que el usuario mini puede leer
#solucion: find . -writable