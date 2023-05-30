
<li>
      <a>minihack</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>

![portada](https://github.com/KermitPurple96/minihack/assets/103221169/1a4c81e6-686b-4695-b3bb-3ea39dd22fb4)

### Installation

1. Install packages
```sh
sudo apt update
sudo apt-get install python3
sudo apt install python3-pip
sudo apt-get install python3-dev libmysqlclient-dev
apt install python3-virtualenv
```

2. Create virtual environment 
```sh
virtualenv env --python=python3
```

3. Activate virtual environment 
```sh
source /home/kermit/minihack/env/bin/activate
```

4. Install libraries
```sh
pip install Flask
pip3 install mysqlclient
pip3 install mysql
pip install -U Flask-WTF
pip install email_validator
pip install Flask-MySQLdb
pip install Werkzeug
pip install Flask-Login
pip install MarkupSafe
pip install bootstrap-flask
```
5. Start Flask server
```sh
/home/user/minihack/start.sh
```

6. Create docker images
```sh
docker build -t entorno /home/user/minihack/dockerfiles/entorno
docker build -t archivos /home/user/minihack/dockerfiles/archivos
docker build -t comandos /home/user/minihack/dockerfiles/comandos
docker build -t networking /home/user/minihack/dockerfiles/networking
docker build -t entorno /home/user/minihack/dockerfiles/usuarios
docker build -t entorno /home/user/minihack/dockerfiles/procesos
docker build -t entorno /home/user/minihack/dockerfiles/pivote
```
7. Start the containers
```sh
cd /home/user/minihack/dockerfiles
docker-compose up -d
```
