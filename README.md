
# Minihack
This is a CTF type web project based on the [https://overthewire.org]OverTheWire web using Flask and docker for the labs.
<p align="center">
  <img src="https://github.com/KermitPurple96/minihack/assets/103221169/1a4c81e6-686b-4695-b3bb-3ea39dd22fb4">
</p>
<p align="center">
  <img src="https://github.com/KermitPurple96/minihack/assets/103221169/79676d56-df46-40e2-aacf-73836b3a3ca8">
</p>
<p align="center">
  <img src="https://github.com/KermitPurple96/minihack/assets/103221169/79f52a22-c009-423a-b018-9d270b2aa9f4">
</p>

### Installation
1. Clone repository
```sh
git clone https://github.com/KermitPurple96/minihack
```
2. Install packages
```sh
sudo apt update
sudo apt -y install wget php php-cgi php-mysqli php-pear php-mbstring libapache2-mod-php php-common php-phpseclib php-mysql
sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl
apt install docker.io -y
apt install docker-compose
sudo apt install mysql-server
sudo apt-get install python3
sudo apt install python3-pip
sudo apt-get install python3-dev libmysqlclient-dev
apt install python3-virtualenv
```

3. Create virtual environment 
```sh
cd /home/kermit/minihack
virtualenv env --python=python3
```

4. Activate virtual environment 
```sh
source /home/kermit/minihack/env/bin/activate
```

5. Install libraries
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
6. Start Flask server
```sh
/home/kermit/minihack/start.sh
```

7. Create docker images
```sh
docker build -t entorno /home/kermit/minihack/dockerfiles/entorno
docker build -t archivos /home/kermit/minihack/dockerfiles/archivos
docker build -t comandos /home/kermit/minihack/dockerfiles/comandos
docker build -t networking /home/kermit/minihack/dockerfiles/networking
docker build -t usuarios /home/kermit/minihack/dockerfiles/usuarios
docker build -t procesos /home/kermit/minihack/dockerfiles/procesos
docker build -t pivote /home/kermit/minihack/dockerfiles/pivote
```
8. Start the containers
```sh
cd /home/kermit/minihack/dockerfiles
docker-compose up -d
```
