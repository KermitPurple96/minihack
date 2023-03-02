from flask import Flask, render_template, request, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from markupsafe import escape 
from flask_mysqldb import MySQL
import subprocess
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect




app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'd7b3956cf05e2074ed69681eaab6a39b'



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'localhost'

modulos = ['home','entorno', 'comandos', 'usuarios', 'networking', 'archivos', 'procesos']

@app.route('/')
def hello():
    return redirect("/home", code=302)

@app.route("/home", methods=['POST', 'GET'])
def inicio():

    data = {
        'titulo': modulos[0],
        'modulos': modulos
    }
    return render_template('index.html', data=data)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    data={
        'titulo': 'register',
        'modulos': modulos
    }
    if form.validate_on_submit():
        flash(f'{form.username.data}', 'success')
        return redirect('/')
    return render_template('register.html', title='register', form=form, data=data)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    data={
        'titulo': 'login',
        'modulos': modulos
    }
    if form.validate_on_submit():
        if form.email.data == 'admin@minihack.com' and form.password.data == 'password':
            return redirect('/')
        else:
            flash(f'Incorrect credentials', 'danger')

    return render_template('login.html', title='login', form=form, data=data)

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

@app.errorhandler(404)
def page_not_found(error):
    data = {
    'titulo': 'not found',
    'modulos': modulos
    }
    return render_template('404.html', data=data), 404

if __name__ == '__main__':
     app.run(debug=True, port=5000)
    #  app.register_error_handler(404, pagina_no_encontrada)
