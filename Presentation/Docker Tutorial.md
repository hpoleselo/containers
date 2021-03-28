# A Gentle Docker Tutorial

This serve as base for a Docker Crash Course

Docker client-server application. The client is our command-line and the server is the daemon running in our computer.

https://youtu.be/t5EfITuFD9w

Proposito dessa Introdução: alguns conceitos que eu aprendi, não fui em baixo nivel e já com hands-on. Complemento da galera sempre é bom

Não é um tecnologia na modinha e que já é bem consolidada inclusive, e sim um paradigma, assi como IDE e Git são must-have para um developer, é uma ferramenta poderosíssima.
Pode ser usado em qualquer projeto, indep. do tamanho.
Compose, Swarm e depois podemos ir Amazon Container Services e Kubernetes.

## Motivation

1. Motivação em Python? Dependências, pyenv (funciona localmente)
2. Programa em Python para fazer requisição de uma página Web

## What Is Docker and How Docker Works

- Why we need Docker? (Tudo isso é feito pois precisamos nos adaptar ao Docker e seus principios, configuração, estando nos conformes do Docker, ela já estará apta pra ser scallable não só no Docker)

  

- Why is Docker so good? (Technical explanation)
  - AuFS, hoje em dia pode ser overlay2, depende do driver do Docker
    That's one of the reasons why Docker containers can be run much faster than VMs!
    The drawback from Docker is that it doesn't give this full isolation like a VM offers (minimal sharing).
  - LXC:recursos globais são wrapped em namespaces, e esses namespaces são visíveis para os processos que rodam com o mesmo namespace. Portanto cada container teria seu napespace e os containers podem se comunicar ou serem isolados. Note que todos os containers/processos estão rodando no mesmo kernel, então temos isolação.

## Terminology

- Container: instância que encapsula o software desejado, containers são criados por imagens, não mantém estado, são meio que dispatched?
- Image: elemento básico de um container, possui estados, pode ser cacheado e reutilizado
- Portas: tanto TCP quanto UDP, de forma que os containers se comuniquem ou para que se comunique com o host OS
- Volume: diretório compartilhado, os dados que conseguimos nos programas rodados dentro do container não são guardados no container (ou pelo menos não é um good practice), we have to output somewhere
- Quando o comando docker run é executado, Linux usa metadata para criar toda a infraestrutura pra montar a imagem, um layer escrevível e rodar o processo. Adicionar `--rm` faz com que o daemon do docker mate o processo, remover toda a arquitetura montada "plumbing" e  o writable layer da imagem



Inicialmente, todas as imagens do Docker são armazenadas como séries de camadas somente leitura, quando é iniciado um container usando essa  imagem, é criada uma nova camada com permissão de escrita.
Quando um  container do Docker é destruído, a imagem continua ainda disponível para ser utilizada, porem ocorre um “reinicio” da imagem, excluindo todas as modificações do container anterior. Isso tudo funciona nas camadas do  Union File System

## Installation

Follow tutorial

1. Baixar o Docker Comunity Edition (docker-ce)
2. Falar sobre as diferentes imagens de Docker: Docker for Windows (Hyper-V) x Docker Toolbox (uses a VM) e Windows Server Containers (que roda os binários do Windows)
3.  `$ sudo systemctl status docker`
4. `$ docker info`
5. Depois de instalado mostrar a localização do Docker: cd /var/lib/docker
6. Falar sobre as imagens, que estão localizadas dentro de /images/overlay e que isso pode variar, no caso ser `overlay` `overlay2` ou `aufs` dependendo do driver que o Docker usou para storage.
7. Já sabemos qual é o driver utilizado pelo /overlay2
8. `$ sudo usermod -aG docker $(whoami)`
9. Todo comando de Docker ter que usar sudo, um saco. É um service instalado no kernel e é inicializado juntamente com outros drivers, o que mostra que Docker é shared com o Kernel e faz uso do kernel, ou seja, não usa um Hypervisor
10. Mostrar pasta 

## First Steps with Docker

1. `$ docker run hello-world`
2. `$ docker pull python:3.8-slim-buster`, `$ docker run python:3.8-slim-buster` mostrar que sem o `--rm` dá ruim, e depois mostrar de forma interativa `-it`
3. `$ docker ps -a` e depois `$ docker rm CONTAINER_ID`
4. Removendo imagens: `$ docker rmi IMAGE_NAME`
5. Checking images
6. `$ docker inspect`
7. Show where the images are stored! `var/lib/docker/overlay2/ca6e3704d9fdfdd681db5c2cad89ff4f1f297284ae089a66b5d3fcd8d9ce5f81/diff/usr/local`
8. Maybe in Python?
9. Mostrar que se não colocar a tag, não funciona e ele fica como none no docker images e fica ocupando espaço
10. Mostrar que instalando python minimal ele acaba não 
11. Mostar ubuntu pull image

Quando o comando docker run é executado, Linux usa metadata para criar toda a infraestrutura pra montar a imagem, um layer escrevível e rodar o processo. Adicionar `--rm` faz com que o daemon do docker mate o processo, remover toda a arquitetura montada "plumbing" e  o writable layer da imagem

## Dockerizing Python Application

#### Simple Dockfile

O volume ele pode ser do tipo anonymous ou named volume.

1. Create a folder which will contain our little project and: hello-docker.py

2. On any folder, create a file called Dockerfile

   ```
   FROM python:3.8-slim-buster
   
   WORKDIR /src
   
   COPY hello-docker.py .
   
   CMD python hello-docker.py
   ```

3. Explicar o que acontece no Dockerfile, sequencial. Pega imagem existente com FROM, com a imagem ele roda o comando RUN para instalação (com Python instalariamos as dependencias) e depois CMD com a sequência de comando que deve ser rodado antes do container é executado.

4. Make change to the Python script and run again.

5. The script doesn't update! We have to attach it to a volume

6. O que iremos fazer aqui é um Bind mount com o Host volume. Compartilhar um diretório do nosso PC (host) para um diretório do contianer, separados por dois pontos, sendo que no final dizemos as operações permitidas!

7. `$ docker run --rm -v $(pwd):/src:rw hello-docker`

8. Agora  veremos que o arquivo é escrito no nosso diretório local

9. E se quisessemos ir desenvolvendo o programa de forma iterativa sem ter que dar build

```
$ docker volume create –name bancomysql
```

```
# Associando um docker a um volume já criado, mas tal volume foi criado n

docker container run –d –v bancomysql:/var/lib/mysql mysql
```



#### Dockerizing our Python application

1. Simple test with Python (show that dependencies are installed and make in an interactive mode) -it
2. Docker build sem o -t para mostrar que fica sem nome
3. Mostrar pelo comando: `$ docker images | wc -l` que a cada build diferente ele cria uma nova imagem
4. `$ docker system prune` pra limpar
5. Docker run, modo interativo
6. Diferenciar Volume e Copy (Testing and Production cases)
7. Se formos colocar data, precisamos de um persitent volume
8. `$ docker volume create NAMEOFVOLUME` , go to the docker info, var and check that the volume has been created!
9. `$ docker run --rm -v $(pwd)/vol:/ourAppData/:rw webpage-req`
10. Gitignore is important for production/deployment! Mainly because we copy some files
11. Mostrar a utilidade de um gitignore (espaço que ocupa)
12. Docker Compose, rodando várias instâncias

Workflow tradicional usando COPY/ADD:

`$ docker build -t webpage-request .`

`$ docker run --rm webpage-request`

diferenciar --rm usar ou não!

`$ docker system prune -a`  will work only if the container has been stopped!

`$ docker image prune -all` por default o Docker não vai remover named images, mesmo se não forem utilizados, esse comando remove imagem inutilizadas





NOTE: `overlay2` is system docker folder, and they may  change it structure anytime. Everything above is based on what i saw in  there. Had to go in docker folder structure only because system was  completely out of space and even wouldn't allow me to ssh into docker  container.

