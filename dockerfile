FROM ubuntu:latest

MAINTAINER kermit "kermitpurple96@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y net-tools \
    sudo \
    iputils-ping \
    iproute2 \
    neovim \
    moreutils \
    curl \
    git \ 
    nano \
    apache2 \
    php \
    openssh-server \
    ufw

RUN useradd -ms /bin/bash mini2 
RUN touch /home/mini2/challenge_1.txt
RUN mkdir /usr/share/scripts
RUN chmod o+t /home/mini2/challenge_1.txt
RUN ln -sf /dev/null ./.bash_history
COPY rockyou.txt /usr/share/scripts
COPY grepScript.py /usr/share/scripts
RUN python3 /usr/share/scripts/grepScript.py
RUN echo 'mini2:frog' | chpasswd

EXPOSE 22 

ENTRYPOINT service ssh start && /bin/bash


