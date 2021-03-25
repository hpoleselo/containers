# A Gentle Docker Tutorial

Docker client-server application. The client is our command-line and the server is the daemon running in our computer.

Falar sobre Docker:

## Motivation

1. Motivação em Python? Dependências, pyenv (funciona localmente)
2. Programa em Python para fazer requisição de uma página Web

## Installation

Follow tutorial

1. Falar sobre as diferentes imagens de Docker: Docker x Docker Toolbox
2. $ docker info
3. Depois de instalado mostrar a localização do Docker: cd /var/lib/docker
4. Falar sobre as imagens, que estão localizadas dentro de /images/overlay e que isso pode variar, no caso ser `overlay` `overlay2` ou `aufs` dependendo do driver que o Docker usou para storage.
5. Já sabemos qual é o driver utilizado pelo /overlay2
6. Todo comando de Docker ter que usar sudo, um saco. É um service instalado no kernel e é inicializado juntamente com outros drivers, o que mostra que Docker é shared com o Kernel e faz uso do kernel, ou seja, não usa um Hypervisor
7. Mostrar pasta 

## First Steps with Docker

1. Pulling images
2. Checking images
3. Show where the images are stored! var/lib/docker/overlay2/ca6e3704d9fdfdd681db5c2cad89ff4f1f297284ae089a66b5d3fcd8d9ce5f81/diff/usr/local
4. Building and running in an interactive mode
5. Maybe in Python?
6. Mostrar que se não colocar a tag, não funciona e ele fica como none no docker images e fica ocupando espaço
7. Mostrar que instalando python minimal ele acaba não 
8. Mostar ubuntu pull image
9. 

## Dockerizing Python Application

1. Criando um Dockerfile
2. Docker build
3. Mostrar pelo comando: `$ docker images | wc -l` que a cada build diferente ele cria uma nova imagem
4. `$ docker system prune` pra limpar
5. Docker run, modo interativo
6. Diferenciar Volume e Copy
7. Mostrar a utilidade de um gitignore (espaço que ocupa)
8. Docker Compose, rodando várias instâncias

Workflow tradicional usando COPY/ADD:

$ docker build -t webpage-request .

$ docker run --rm webpage-request

diferenciar --rm usar ou não!

docker system prune -a will work only if the container has been stopped!

docker image prune -all por default o Docker não vai remover named images, mesmo se não forem utilizados, esse comando remove imagem inutilizadas













Muito espaço sendo ocupado por overlay2:

also had problems with rapidly growing `overlay2`

`/var/lib/docker/overlay2` - is a folder where docker store writable layers for your container. `docker system prune -a` - may work only if container is stopped and removed.

in my i was able to figure out what consumes space by going into `overlay2` and investigating.

that folder contains other hash named folders. each of those has several folders including `diff` folder.

`diff` folder - contains actual difference written by a  container with exact folder structure as your container (at least it was in my case - ubuntu 18...)

**so i've used `du -hsc /var/lib/docker/overlay2/LONGHASHHHHHHH/diff/tmp` to figure out that `/tmp` inside of my container is the folder which gets polluted**.

so as a workaround i've used `-v /tmp/container-data/tmp:/tmp` parameter for `docker run` command to map inner `/tmp` folder to host and setup a cron on host to cleanup that folder.

cron task was simple:

- `sudo nano /etc/crontab`
- `*/30 * * * * root rm -rf /tmp/container-data/tmp/*`
- `save and exit`

NOTE: `overlay2` is system docker folder, and they may  change it structure anytime. Everything above is based on what i saw in  there. Had to go in docker folder structure only because system was  completely out of space and even wouldn't allow me to ssh into docker  container.

