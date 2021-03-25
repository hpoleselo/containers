# A Gentle Docker Tutorial

This serve as base for a Docker Crash Course

Docker client-server application. The client is our command-line and the server is the daemon running in our computer.

## Motivation

1. Motivação em Python? Dependências, pyenv (funciona localmente)
2. Programa em Python para fazer requisição de uma página Web



## What Is Docker and How Docker Works

- Why is Docker so good?
  - AuFS, hoje em dia pode ser overlay2, depende do driver do Docker
  - LXC

## Terminology

- Container: instância que encapsula o software desejado, containers são criados por imagens, não mantém estado, são meio que dispatched?
- Image: elemento básico de um container, possui estados, pode ser cacheado e reutilizado
- Portas: tanto TCP quanto UDP, de forma que os containers se comuniquem ou para que se comunique com o host OS
- Volume: diretório compartilhado, os dados que conseguimos nos programas rodados dentro do container não são guardados no container (ou pelo menos não é um good practice), we have to output somewhere

## Installation

Follow tutorial

1. Falar sobre as diferentes imagens de Docker: Docker x Docker Toolbox
2. Mostrar serviços
3. `$ docker info`
4. Depois de instalado mostrar a localização do Docker: cd /var/lib/docker
5. Falar sobre as imagens, que estão localizadas dentro de /images/overlay e que isso pode variar, no caso ser `overlay` `overlay2` ou `aufs` dependendo do driver que o Docker usou para storage.
6. Já sabemos qual é o driver utilizado pelo /overlay2
7. Todo comando de Docker ter que usar sudo, um saco. É um service instalado no kernel e é inicializado juntamente com outros drivers, o que mostra que Docker é shared com o Kernel e faz uso do kernel, ou seja, não usa um Hypervisor
8. Mostrar pasta 

## First Steps with Docker

1. `$ docker run hello-world`
2. `$ docker pull python:3.8-slim-buster`, `$ docker run python:3.8-slim-buster` mostrar que sem o `--rm` dá ruim, e depois mostrar de forma interativa `-it`
3. `$ docker ps -a` e depois `$ docker rm CONTAINER_ID`
4. Pulling images
5. Checking images
6. Show where the images are stored! `var/lib/docker/overlay2/ca6e3704d9fdfdd681db5c2cad89ff4f1f297284ae089a66b5d3fcd8d9ce5f81/diff/usr/local`
7. Maybe in Python?
8. Mostrar que se não colocar a tag, não funciona e ele fica como none no docker images e fica ocupando espaço
9. Mostrar que instalando python minimal ele acaba não 
10. Mostar ubuntu pull image

Quando o comando docker run é executado, Linux usa metadata para criar toda a infraestrutura pra montar a imagem, um layer escrevível e rodar o processo. Adicionar `--rm` faz com que o daemon do docker mate o processo, remover toda a arquitetura montada "plumbing" e  o writable layer da imagem

## Dockerizing Python Application

#### Simple Dockfile

1. On any folder, create a file called Dockerfile

   ```
   FROM ubuntu
   RUN apt update && apt install -y cowsay
   CMD ["/usr/games/cowsay", "Dockerfiles are cool!"]
   ```

2. Explicar o que acontece no Dockerfile, sequencial. Pega imagem existente com FROM, com a imagem ele roda o comando RUN para instalação (com Python instalariamos as dependencias) e depois CMD com a sequência de comando que deve ser rodado antes do container é executado.

3. `$ docker build -t cowsaw .`

4. `$ docker run --rm cowsay`

#### Dockerizing our Python application

1. Simple test with Python (show that dependencies are installed and make in an interactive mode) -it
2. Docker build sem o -t para mostrar que fica sem nome
3. Mostrar pelo comando: `$ docker images | wc -l` que a cada build diferente ele cria uma nova imagem
4. `$ docker system prune` pra limpar
5. Docker run, modo interativo
6. Diferenciar Volume e Copy (Testing and Production cases)
7. Se formos colocar data, precisamos de um persitent volume
8. Mostrar a utilidade de um gitignore (espaço que ocupa)
9. Docker Compose, rodando várias instâncias

Workflow tradicional usando COPY/ADD:

`$ docker build -t webpage-request .`

`$ docker run --rm webpage-request`

diferenciar --rm usar ou não!

`$ docker system prune -a`  will work only if the container has been stopped!

`$ docker image prune -all` por default o Docker não vai remover named images, mesmo se não forem utilizados, esse comando remove imagem inutilizadas





NOTE: `overlay2` is system docker folder, and they may  change it structure anytime. Everything above is based on what i saw in  there. Had to go in docker folder structure only because system was  completely out of space and even wouldn't allow me to ssh into docker  container.

