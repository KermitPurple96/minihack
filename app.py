from flask import Flask, render_template, request, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from markupsafe import escape 
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'd7b3956cf05e2074ed69681eaab6a39b'


modulos = ['home','entorno', 'comandos', 'usuarios', 'networking', 'archivos', 'procesos', 'challenges']

@app.route('/')
def hello():
    return redirect("/home", code=302)

#LANDING

@app.route("/home", methods=['POST', 'GET'])
def inicio():

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
    data={
        'titulo': 'login',
        'modulos': modulos
    }
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        return render_template('login.html', title='login', data=data)
    else:
        return render_template('login.html', title='login', data=data)

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
