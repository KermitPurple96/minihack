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

#@socketio.on('event')
#def event(flag, code):
#    print("data recibida: " + flag + code)
#    emit('event', 'RECIBIDO');
#    cur = mysql.connection.cursor()
#    flag_id = "SELECT flag FROM flags WHERE flag_id = '%d';"
#    data = (code)
#    cur.execute(flag_id, data)
#    mysql.connection.commit()

#    if flag == flag_id:
#        cur.execute("UPDATE users SET flag_%d = True WHERE username = '%s';", (code, session['username']))
#        cur.close()
       
#    else:
#        cur.close()


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
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            data = (username, email, pass1)
            cur.execute(sql, data)
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

@app.get('/challenges/entorno')
def chall_entorno():
    data = {
        'titulo': modulos[1],
        'modulos': modulos
    }
    return render_template('chall_entorno.html', data=data)

@app.get('/challenges/comandos')
def chall_comandos():
    data = {
        'titulo': modulos[2],
        'modulos': modulos,
    }
    return render_template('chall_comandos.html', data=data)

@app.get('/challenges/networking')
def chall_networking():
    data = {
        'titulo': modulos[4],
        'modulos': modulos
    }
    return render_template('chall_networking.html', data=data)

@app.get('/challenges/procesos')
def chall_procesos():
    data = {
        'titulo': modulos[6],
        'modulos': modulos
    }
    return render_template('chall_procesos.html', data=data)

@app.get('/challenges/usuarios')
def chall_usuarios():
    data = {
        'titulo': modulos[3],
        'modulos': modulos
    }
    return render_template('chall_usuarios.html', data=data)

@app.get('/challenges/archivos')
def chall_archivos():
    data = {
        'titulo': modulos[5],
        'modulos': modulos
    }
    return render_template('chall_archivos.html', data=data)

# 404

@app.errorhandler(404)
def page_not_found(error):
    data = {
    'titulo': 'not found',
    'modulos': modulos
    }
    return render_template('404.html', data=data), 404

if __name__ == '__main__':
     app.run(host='192.168.0.115', debug=True, port=5000)
    #  app.register_error_handler(404, pagina_no_encontrada)
