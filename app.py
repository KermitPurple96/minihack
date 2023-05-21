from flask import Flask, render_template, request, url_for, flash, redirect, session
from forms import RegistrationForm, LoginForm
from markupsafe import escape 
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask_login import UserMixin, login_manager, login_user, login_required, logout_user, current_user
import forms



app = Flask(__name__)
mysql = MySQL(app)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = forms.SECRET_KEY
app.config['MYSQL_HOST'] = forms.MYSQL_HOST
app.config['MYSQL_USER'] = forms.MYSQL_USER
app.config['MYSQL_PASSWORD'] = forms.MYSQL_PASSWORD
app.config['MYSQL_DB'] = forms.MYSQL_DB
#socketio = SocketIO(app)

modulos = ['home','entorno', 'comandos', 'usuarios', 'networking', 'archivos', 'procesos', 'challenges']

@app.route('/')
def hello():
    return redirect("/home", code=302)

#404

@app.errorhandler(404)
def page_not_found(error):
    data = {
    'titulo': 'not found',
    'modulos': modulos
    }
    return render_template('404.html', data=data), 404

#LANDING

@app.route("/home", methods=['POST', 'GET'])
def home():

    data = {
        'titulo': modulos[0],
        'modulos': modulos
    }
    return render_template('index.html', data=data)

@app.route("/home/learning", methods=['POST', 'GET'])
def learning():

    data = {
        'titulo': modulos[0],
        'modulos': modulos
    }
    return render_template('learning.html', data=data)

#PAGINAS LOGIN Y REGISTER

@app.route('/register', methods=['POST', 'GET'])
def register():
    data={
        'titulo': 'register',
        'modulos': modulos
    }
   
    if request.method == "POST":
    
        email = request.form['email']
        username = request.form['username']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']

        if email and username and pass1 and pass2 and pass1 == pass2:

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (username, email, password) VALUES ('{}', '{}', '{}')".format(username, email, pass1))
            cur.execute("select id from users ORDER BY id DESC LIMIT 1;")
            #cur.execute("INSERT INTO owned_flags (id_user) VALUES ('{}')").format(last_user)
            last_user = cur.fetchone()[0]
            cur.execute("INSERT INTO owned_flags (id_user, flag_entorno_1, flag_entorno_2, flag_entorno_3, flag_entorno_4, flag_entorno_5, flag_comandos_1, flag_comandos_2, flag_comandos_3, flag_comandos_4, flag_comandos_5, flag_usuarios_1, flag_usuarios_2, flag_usuarios_3, flag_usuarios_4, flag_usuarios_5, flag_networking_1, flag_networking_2, flag_networking_3, flag_networking_4, flag_networking_5, flag_archivos_1, flag_archivos_2, flag_archivos_3, flag_archivos_4, flag_archivos_5, flag_procesos_1, flag_procesos_2, flag_procesos_3, flag_procesos_4, flag_procesos_5) VALUES ({}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);".format(last_user))
            print(last_user)
            #cur.execute("UPDATE owned_flags set id_user = '{}' flag_entorno_1 = 0 , flag_entorno_2 = 0 , flag_entorno_3 = 0 , flag_entorno_4 = 0 , flag_entorno_5 = 0 , flag_comandos_1 = 0 , flag_comandos_2 = 0 , flag_comandos_3 = 0 , flag_comandos_4 = 0 , flag_comandos_5 = 0 , flag_usuarios_1 = 0 , flag_usuarios_2 = 0 , flag_usuarios_3 = 0 , flag_usuarios_4 = 0 , flag_usuarios_5 = 0 , flag_networking_1 = 0 , flag_networking_2 = 0 , flag_networking_3 = 0 , flag_networking_4 = 0 , flag_networking_5 = 0 , flag_archivos_1 = 0 , flag_archivos_2 = 0 , flag_archivos_3 = 0 , flag_archivos_4 = 0 , flag_archivos_5 = 0 , flag_procesos_1 = 0 , flag_procesos_2 = 0 , flag_procesos_3 = 0 , flag_procesos_4 = 0 , flag_procesos_5 = 0 where id_user = '{}';".format(last_user))

            #data = (username, email, pass1, '0', '0', '0', '0', '0')
            #cur.execute("UPDATE users SET {} = {} WHERE username = '{}'".format(num_flag, one, username))
            
            #cur.execute(sql, data)
            mysql.connection.commit()
            
            session['email'] = email
            session['username'] = username
            cur.close()
                
            return render_template('index.html', data=data, message="Successfully register")
        else:
            return render_template('resgister.html', data=data, message="Invalid data")
    else:
        return render_template('register.html', data=data)
    

#@app.route("/login", methods=['POST', 'GET'])
#def login():
#    data = {
#        'titulo': modulos[1],
#        'modulos': modulos
#    }
#    return render_template('login.html', title='login', data=data)


@app.route("/login", methods=['POST', 'GET'])
def login():

    data={
        'titulo': 'login',
        'modulos': modulos
    }
    if request.method == "POST":
    
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * from users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()

        if user is not None:
            session['email'] = email
            session['username'] = user[1]

            return render_template('index.html', data=data, message="Successfully login")
        else:
            return render_template('login.html', data=data, message="credenciales incorrectas")
    else:
        return render_template('login.html', data=data)

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect("/home")

#PAGINAS

@app.get('/entorno')
def entorno():
    data = {
        'titulo': modulos[1],
        'modulos': modulos
    }
    return render_template('entorno.html', data=data)

@app.get('/comandos')
def comandos():
    data = {
        'titulo': modulos[2],
        'modulos': modulos
    }
    return render_template('comandos.html', data=data)

@app.get('/usuarios')
def usuarios():
    data = {
        'titulo': modulos[3],
        'modulos': modulos
    }
    return render_template('usuarios.html', data=data)

@app.get('/networking')
def networking():
    data = {
        'titulo': modulos[4],
        'modulos': modulos
    }
    return render_template('networking.html', data=data)

@app.get('/archivos')
def archivos():
    data = {
        'titulo': modulos[5],
        'modulos': modulos
    }
    return render_template('archivos.html', data=data)

@app.get('/procesos')
def procesos():
    data = {
        'titulo': modulos[6],
        'modulos': modulos
    }
    return render_template('procesos.html', data=data)

# CHALLENGES

@app.get('/challenges')
def challenges():
    data = {
        'titulo': modulos[7],
        'modulos': modulos
    }
    return render_template('challenges.html', data=data)

@app.get('/challenges/conexion_ssh')
def challengesssh():
    data = {
        'titulo': modulos[7],
        'modulos': modulos
    }
    return render_template('conexion_ssh.html', data=data)


# CHALLENGES_ENTORNO

@app.route('/challenges/entorno', methods=['POST', 'GET'])
def chall_entorno():
    data = {
        'titulo': modulos[1],
        'modulos': modulos
    }
    data_flags = []
    data_sols = []
    num = ""
    flag = ""

    if request.method == "POST":

        num = request.form['num']
        print("NUM")
        print(num)
        flag = request.form['flag']
        username = session['username']
        print(username)

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_entorno FROM flags")
        sol = cur.fetchall()
        cur.close()           

        #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_entorno FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        
        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        owned_flags = []
        owned_sols = []
        j = 0

        if flag:
            cur = mysql.connection.cursor()
            cur.execute("SELECT flag_entorno FROM flags WHERE flag_id = %s", (num))
            real_flag = cur.fetchone()
            cur.close()

            num_flag = ("flag_entorno_" + num)
            #print(one)
            print(num_flag)
            username = session['username']
            print(username)

            #Flags que ya ha conseguido el usuario (0 o 1)
            #mysql.connection.commit()
            #cur.close()
            #cur = mysql.connection.cursor()
            #cur.execute("SELECT flag_1,flag_2,flag_3,flag_4,flag_5 FROM users where username = %s", [username])
            #own_flags = []
            #own_flags = cur.fetchall()[0]
            print("DDD")
            print(real_flag[0])
            print(flag)
            


            if real_flag[0] == flag:

                #El usuario a conseguido una nueva flag ->
                cur = mysql.connection.cursor()
                cur.execute("UPDATE owned_flags SET {} = {} WHERE id_user = '{}'".format(num_flag, 1, id_user))
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_entorno_1,flag_entorno_2,flag_entorno_3,flag_entorno_4,flag_entorno_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                

                return render_template('chall_entorno.html', data=data, num=num, code='1', flag=flag, data_sols=data_sols, data_flags=data_flags)
            
            else:

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_entorno_1,flag_entorno_2,flag_entorno_3,flag_entorno_4,flag_entorno_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)


                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                return render_template('chall_entorno.html', data=data, num=num, code='0', flag=flag, data_flags=data_flags, data_sols=data_sols)
    
    else:

        username = session['username']
        
        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()
        print(id)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT flag_entorno_1,flag_entorno_2,flag_entorno_3,flag_entorno_4,flag_entorno_5 FROM owned_flags where id_user = %s", [id_user])
        own_flags = []
        own_flags = cur.fetchall()[0]
        print("OWN FLAGS")
        print(own_flags)


        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_entorno FROM flags")
        sol = cur.fetchall()
        cur.close()

                #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_entorno FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        owned_flags = []
        owned_sols = []
        j = 0
        print("own_flags")
        print(own_flags)

        for i in own_flags:
            print(i)
            if i != 0:
                owned_flags.append(fl[j])
                owned_sols.append(sol[j])
            else:
                owned_flags.append("0")
                owned_sols.append("0")
            j += 1

        print("owned_flags")
        print(owned_flags)

        for elemento in owned_flags:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_flags.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_flags.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_flags.append(elemento)
        
        for elemento in owned_sols:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_sols.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_sols.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_sols.append(elemento)
                    
                    
        print(data_flags)
        print(data_sols)

        return render_template('chall_entorno.html', data=data, num=num, code='2', flag=flag, data_flags=data_flags, data_sols=data_sols)


# CHALLENGES_COMANDOS

@app.route('/challenges/comandos', methods=['POST', 'GET'])
def chall_comandos():
    data = {
        'titulo': modulos[2],
        'modulos': modulos,
    }

    data_flags = []
    data_sols = []
    num = ""
    flag = ""

    if request.method == "POST":

        num = request.form['num']
        print("NUM")
        print(num)
        flag = request.form['flag']
        username = session['username']
        print(username)

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_comandos FROM flags")
        sol = cur.fetchall()
        cur.close()           

        #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_comandos FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        owned_flags = []
        owned_sols = []
        j = 0

        if flag:
            cur = mysql.connection.cursor()
            cur.execute("SELECT flag_comandos FROM flags WHERE flag_id = %s", (num))
            real_flag = cur.fetchone()

            num_flag = ("flag_comandos_" + num)
            
            print(num_flag)
            username = session['username']
            print(username)

            #Flags que ya ha conseguido el usuario (0 o 1)
            #mysql.connection.commit()
            #cur.close()
            #cur = mysql.connection.cursor()
            #cur.execute("SELECT flag_1,flag_2,flag_3,flag_4,flag_5 FROM users where username = %s", [username])
            #own_flags = []
            #own_flags = cur.fetchall()[0]
            print("DDD")
            print(real_flag[0])
            print(flag)

            if real_flag[0] == flag:

                #El usuario a conseguido una nueva flag ->
                cur = mysql.connection.cursor()
                cur.execute("UPDATE owned_flags SET {} = {} WHERE id_user = '{}'".format(num_flag, 1, id_user))
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_comandos_1,flag_comandos_2,flag_comandos_3,flag_comandos_4,flag_comandos_5 from owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                

                return render_template('chall_comandos.html', data=data, num=num, code='1', flag=flag, data_sols=data_sols, data_flags=data_flags)
            else:

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_comandos_1,flag_comandos_2,flag_comandos_3,flag_comandos_4,flag_comandos_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                return render_template('chall_comandos.html', data=data, num=num, code='0', flag=flag, data_flags=data_flags, data_sols=data_sols)
    else:
        username = session['username']

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT flag_comandos_1,flag_comandos_2,flag_comandos_3,flag_comandos_4,flag_comandos_5 FROM owned_flags where id_user = %s", [id_user])
        own_flags = []
        own_flags = cur.fetchall()[0]

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_comandos FROM flags")
        sol = cur.fetchall()
        cur.close()

                #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_comandos FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        owned_flags = []
        owned_sols = []
        j = 0

        for i in own_flags:
            print(i)
            if i != 0:
                owned_flags.append(fl[j])
                owned_sols.append(sol[j])
            else:
                owned_flags.append("0")
                owned_sols.append("0")
            j += 1



        for elemento in owned_flags:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_flags.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_flags.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_flags.append(elemento)
        
        for elemento in owned_sols:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_sols.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_sols.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_sols.append(elemento)
                    
                    
        print(data_flags)
        print(data_sols)

        return render_template('chall_comandos.html', data=data, num=num, code='2', flag=flag, data_flags=data_flags, data_sols=data_sols)



# CHALLENGES_USUARIOS


@app.route('/challenges/usuarios', methods=['POST', 'GET'])
def chall_usuarios():
    data = {
        'titulo': modulos[3],
        'modulos': modulos
    }
    data_flags = []
    data_sols = []
    num = ""
    flag = ""

    if request.method == "POST":

        num = request.form['num']
        print("NUM")
        print(num)
        flag = request.form['flag']
        username = session['username']
        print(username)

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_usuarios FROM flags")
        sol = cur.fetchall()
        cur.close()           

        #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_usuarios FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        owned_flags = []
        owned_sols = []
        j = 0

        if flag:
            cur = mysql.connection.cursor()
            cur.execute("SELECT flag_usuarios FROM flags WHERE flag_id = %s", (num))
            real_flag = cur.fetchone()

            one = '1'
            num_flag = ("flag_usuarios_" + num)
            print(one)
            print(num_flag)
            username = session['username']
            print(username)

            #Flags que ya ha conseguido el usuario (0 o 1)
            #mysql.connection.commit()
            #cur.close()
            #cur = mysql.connection.cursor()
            #cur.execute("SELECT flag_1,flag_2,flag_3,flag_4,flag_5 FROM users where username = %s", [username])
            #own_flags = []
            #own_flags = cur.fetchall()[0]
            print("DDD")
            print(real_flag[0])
            print(flag)

            if real_flag[0] == flag:

                #El usuario a conseguido una nueva flag ->
                cur = mysql.connection.cursor()
                cur.execute("UPDATE owned_flags SET {} = {} WHERE id_user = '{}'".format(num_flag, 1, id_user))
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_usuarios_1,flag_usuarios_2,flag_usuarios_3,flag_usuarios_4,flag_usuarios_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                

                return render_template('chall_usuarios.html', data=data, num=num, code='1', flag=flag, data_sols=data_sols, data_flags=data_flags)
            
            else:

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_usuarios_1,flag_usuarios_2,flag_usuarios_3,flag_usuarios_4,flag_usuarios_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)


                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                return render_template('chall_usuarios.html', data=data, num=num, code='0', flag=flag, data_flags=data_flags, data_sols=data_sols)
    
    else:

        username = session['username']

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT flag_usuarios_1,flag_usuarios_2,flag_usuarios_3,flag_usuarios_4,flag_usuarios_5 FROM owned_flags where id_user = %s", [id_user])
        own_flags = []
        own_flags = cur.fetchall()[0]
        print("OWN FLAGS")
        print(own_flags)


        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_usuarios FROM flags")
        sol = cur.fetchall()
        cur.close()

                #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_usuarios FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        owned_flags = []
        owned_sols = []
        j = 0
        print("own_flags")
        print(own_flags)

        for i in own_flags:
            print(i)
            if i != 0:
                owned_flags.append(fl[j])
                owned_sols.append(sol[j])
            else:
                owned_flags.append("0")
                owned_sols.append("0")
            j += 1

        print("owned_flags")
        print(owned_flags)

        for elemento in owned_flags:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_flags.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_flags.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_flags.append(elemento)
        
        for elemento in owned_sols:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_sols.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_sols.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_sols.append(elemento)
                    
                    
        print(data_flags)
        print(data_sols)

        return render_template('chall_usuarios.html', data=data, num=num, code='2', flag=flag, data_flags=data_flags, data_sols=data_sols)


    return render_template('chall_usuarios.html', data=data)


# NETWORKING

@app.route('/challenges/networking', methods=['POST', 'GET'])
def chall_networking():
    data = {
        'titulo': modulos[4],
        'modulos': modulos
    }
    data_flags = []
    data_sols = []
    num = ""
    flag = ""

    if request.method == "POST":

        num = request.form['num']
        print("NUM")
        print(num)
        flag = request.form['flag']
        username = session['username']
        print(username)

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_networking FROM flags")
        sol = cur.fetchall()
        cur.close()           

        #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_networking FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        owned_flags = []
        owned_sols = []
        j = 0

        if flag:
            cur = mysql.connection.cursor()
            cur.execute("SELECT flag_networking FROM flags WHERE flag_id = %s", (num))
            real_flag = cur.fetchone()

            num_flag = ("flag_networking_" + num)
            
            print(num_flag)
            username = session['username']
            print(username)

            #Flags que ya ha conseguido el usuario (0 o 1)
            #mysql.connection.commit()
            #cur.close()
            #cur = mysql.connection.cursor()
            #cur.execute("SELECT flag_1,flag_2,flag_3,flag_4,flag_5 FROM users where username = %s", [username])
            #own_flags = []
            #own_flags = cur.fetchall()[0]
            print("DDD")
            print(real_flag[0])
            print(flag)

            if real_flag[0] == flag:

                #El usuario a conseguido una nueva flag ->
                cur = mysql.connection.cursor()
                cur.execute("UPDATE owned_flags SET {} = {} WHERE id_user = '{}'".format(num_flag, 1, id_user))
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_networking_1,flag_networking_2,flag_networking_3,flag_networking_4,flag_networking_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                

                return render_template('chall_networking.html', data=data, num=num, code='1', flag=flag, data_sols=data_sols, data_flags=data_flags)
            
            else:

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_networking_1,flag_networking_2,flag_networking_3,flag_networking_4,flag_networking_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)


                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                return render_template('chall_networking.html', data=data, num=num, code='0', flag=flag, data_flags=data_flags, data_sols=data_sols)
    
    else:

        username = session['username']

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT flag_networking_1,flag_networking_2,flag_networking_3,flag_networking_4,flag_networking_5 FROM owned_flags where id_user = %s", [id_user])
        own_flags = []
        own_flags = cur.fetchall()[0]
        print("OWN FLAGS")
        print(own_flags)


        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_networking FROM flags")
        sol = cur.fetchall()
        cur.close()

                #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_networking FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        owned_flags = []
        owned_sols = []
        j = 0
        print("own_flags")
        print(own_flags)

        for i in own_flags:
            print(i)
            if i != 0:
                owned_flags.append(fl[j])
                owned_sols.append(sol[j])
            else:
                owned_flags.append("0")
                owned_sols.append("0")
            j += 1

        print("owned_flags")
        print(owned_flags)

        for elemento in owned_flags:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_flags.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_flags.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_flags.append(elemento)
        
        for elemento in owned_sols:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_sols.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_sols.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_sols.append(elemento)
                    
                    
        print(data_flags)
        print(data_sols)

        return render_template('chall_networking.html', data=data, num=num, code='2', flag=flag, data_flags=data_flags, data_sols=data_sols)

    return render_template('chall_networking.html', data=data)



@app.route('/challenges/archivos', methods=['POST', 'GET'])
def chall_archivos():
    data = {
        'titulo': modulos[5],
        'modulos': modulos
    }
    data_flags = []
    data_sols = []
    num = ""
    flag = ""

    if request.method == "POST":

        num = request.form['num']
        print("NUM")
        print(num)
        flag = request.form['flag']
        username = session['username']
        print(username)

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_archivos FROM flags")
        sol = cur.fetchall()
        cur.close()           

        #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_archivos FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        owned_flags = []
        owned_sols = []
        j = 0

        if flag:
            cur = mysql.connection.cursor()
            cur.execute("SELECT flag_archivos FROM flags WHERE flag_id = %s", (num))
            real_flag = cur.fetchone()

            num_flag = ("flag_archivos_" + num)
            
            print(num_flag)
            username = session['username']
            print(username)

            #Flags que ya ha conseguido el usuario (0 o 1)
            #mysql.connection.commit()
            #cur.close()
            #cur = mysql.connection.cursor()
            #cur.execute("SELECT flag_1,flag_2,flag_3,flag_4,flag_5 FROM users where username = %s", [username])
            #own_flags = []
            #own_flags = cur.fetchall()[0]
            print("DDD")
            print(real_flag[0])
            print(flag)

            if real_flag[0] == flag:

                #El usuario a conseguido una nueva flag ->
                cur = mysql.connection.cursor()
                cur.execute("UPDATE owned_flags SET {} = {} WHERE id_user = '{}'".format(num_flag, 1, id_user))
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_archivos_1,flag_archivos_2,flag_archivos_3,flag_archivos_4,flag_archivos_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                

                return render_template('chall_archivos.html', data=data, num=num, code='1', flag=flag, data_sols=data_sols, data_flags=data_flags)
            
            else:

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_archivos_1,flag_archivos_2,flag_archivos_3,flag_archivos_4,flag_archivos_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)


                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                return render_template('chall_archivos.html', data=data, num=num, code='0', flag=flag, data_flags=data_flags, data_sols=data_sols)
    
    else:

        username = session['username']

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT flag_archivos_1,flag_archivos_2,flag_archivos_3,flag_archivos_4,flag_archivos_5 FROM owned_flags where id_user = %s", [id_user])
        own_flags = []
        own_flags = cur.fetchall()[0]
        print("OWN FLAGS")
        print(own_flags)


        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_archivos FROM flags")
        sol = cur.fetchall()
        cur.close()

                #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_archivos FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        owned_flags = []
        owned_sols = []
        j = 0
        print("own_flags")
        print(own_flags)

        for i in own_flags:
            print(i)
            if i != 0:
                owned_flags.append(fl[j])
                owned_sols.append(sol[j])
            else:
                owned_flags.append("0")
                owned_sols.append("0")
            j += 1

        print("owned_flags")
        print(owned_flags)

        for elemento in owned_flags:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_flags.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_flags.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_flags.append(elemento)
        
        for elemento in owned_sols:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_sols.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_sols.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_sols.append(elemento)
                    
                    
        print(data_flags)
        print(data_sols)

        return render_template('chall_archivos.html', data=data, num=num, code='2', flag=flag, data_flags=data_flags, data_sols=data_sols)

    return render_template('chall_archivos.html', data=data)

@app.route('/challenges/procesos', methods=['POST', 'GET'])
def chall_procesos():
    data = {
        'titulo': modulos[6],
        'modulos': modulos
    }
    data_flags = []
    data_sols = []
    num = ""
    flag = ""

    if request.method == "POST":

        num = request.form['num']
        print("NUM")
        print(num)
        flag = request.form['flag']
        username = session['username']
        print(username)

        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_procesos FROM flags")
        sol = cur.fetchall()
        cur.close()           

        #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_procesos FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        owned_flags = []
        owned_sols = []
        j = 0

        if flag:
            cur = mysql.connection.cursor()
            cur.execute("SELECT flag_procesos FROM flags WHERE flag_id = %s", (num))
            real_flag = cur.fetchone()

            num_flag = ("flag_procesos_" + num)
            
            print(num_flag)
            username = session['username']
            print(username)

            #Flags que ya ha conseguido el usuario (0 o 1)
            #mysql.connection.commit()
            #cur.close()
            #cur = mysql.connection.cursor()
            #cur.execute("SELECT flag_1,flag_2,flag_3,flag_4,flag_5 FROM users where username = %s", [username])
            #own_flags = []
            #own_flags = cur.fetchall()[0]
            print("DDD")
            print(real_flag[0])
            print(flag)

            if real_flag[0] == flag:

                #El usuario a conseguido una nueva flag ->
                cur = mysql.connection.cursor()
                cur.execute("UPDATE owned_flags SET {} = {} WHERE id_user = '{}'".format(num_flag, 1, id_user))
                mysql.connection.commit()
                cur.close()

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_procesos_1,flag_procesos_2,flag_procesos_3,flag_procesos_4,flag_procesos_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)

                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                

                return render_template('chall_procesos.html', data=data, num=num, code='1', flag=flag, data_sols=data_sols, data_flags=data_flags)
            
            else:

                cur = mysql.connection.cursor()
                cur.execute("SELECT flag_procesos_1,flag_procesos_2,flag_procesos_3,flag_procesos_4,flag_procesos_5 FROM owned_flags where id_user = %s", [id_user])
                own_flags = []
                own_flags = cur.fetchall()[0]
                print("OWN FLAGS")
                print(own_flags)


                for i in own_flags:
                    print(i)
                    if i != 0:
                        owned_flags.append(fl[j])
                        owned_sols.append(sol[j])
                    else:
                        owned_flags.append("0")
                        owned_sols.append("0")
                    j += 1



                for elemento in owned_flags:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_flags.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_flags.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_flags.append(elemento)
                
                for elemento in owned_sols:
                    if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                        data_sols.append(elemento[0])
                    elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                        data_sols.append(elemento[1:-1])
                    elif isinstance(elemento, str) and elemento.isdigit():
                        data_sols.append(elemento)
                            
                            
                print(data_flags)
                print(data_sols)
                return render_template('chall_procesos.html', data=data, num=num, code='0', flag=flag, data_flags=data_flags, data_sols=data_sols)
    
    else:

        username = session['username']

        #ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users where username = '{}'".format(username))
        id_user = cur.fetchone()[0]
        print(id)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT flag_procesos_1,flag_procesos_2,flag_procesos_3,flag_procesos_4,flag_procesos_5 FROM owned_flags where id_user = %s", [id_user])
        own_flags = []
        own_flags = cur.fetchall()[0]
        print("OWN FLAGS")
        print(own_flags)


        #Clave para conectarse al siguiente nivel
        cur = mysql.connection.cursor()
        cur.execute("SELECT sol_procesos FROM flags")
        sol = cur.fetchall()
        cur.close()

                #Flags
        flgs = mysql.connection.cursor()
        flgs.execute("SELECT flag_procesos FROM flags")
        fl = flgs.fetchall()
        cur.close()
        #print(fl)
        #print(own_flags)
        #print(sol)
        owned_flags = []
        owned_sols = []
        j = 0
        print("own_flags")
        print(own_flags)

        for i in own_flags:
            print(i)
            if i != 0:
                owned_flags.append(fl[j])
                owned_sols.append(sol[j])
            else:
                owned_flags.append("0")
                owned_sols.append("0")
            j += 1

        print("owned_flags")
        print(owned_flags)

        for elemento in owned_flags:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_flags.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_flags.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_flags.append(elemento)
        
        for elemento in owned_sols:
            if isinstance(elemento, tuple) and len(elemento) == 1 and isinstance(elemento[0], str):
                data_sols.append(elemento[0])
            elif isinstance(elemento, str) and elemento.startswith("'") and elemento.endswith("'"):
                data_sols.append(elemento[1:-1])
            elif isinstance(elemento, str) and elemento.isdigit():
                data_sols.append(elemento)
                    
                    
        print(data_flags)
        print(data_sols)

        return render_template('chall_procesos.html', data=data, num=num, code='2', flag=flag, data_flags=data_flags, data_sols=data_sols)

    return render_template('chall_procesos.html', data=data)



if __name__ == '__main__':
     app.run(sdebug=True, port=5000)
    #  app.register_error_handler(404, pagina_no_encontrada)
