
# minihack![portada](https://github.com/KermitPurple96/minihack/assets/103221169/1a4c81e6-686b-4695-b3bb-3ea39dd22fb4)

Install packages
sudo apt update
sudo apt-get install python3
sudo apt install python3-pip
sudo apt-get install python3-dev libmysqlclient-dev
apt install python3-virtualenv

Create virtual environment 
virtualenv env --python=python3

Activate virtual environment 
source /home/kermit/minihack/env/bin/activate

Install libraries
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

/home/user/minihack/start.sh

Create docker images
docker build -t entorno /home/user/minihack/dockerfiles/entorno
docker build -t archivos /home/user/minihack/dockerfiles/archivos
docker build -t comandos /home/user/minihack/dockerfiles/comandos
docker build -t networking /home/user/minihack/dockerfiles/networking
docker build -t entorno /home/user/minihack/dockerfiles/usuarios
docker build -t entorno /home/user/minihack/dockerfiles/procesos
docker build -t entorno /home/user/minihack/dockerfiles/pivote

cd /home/user/minihack/dockerfiles
docker-compose up -d
