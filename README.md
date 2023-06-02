# Docker Command Sheet

Commands used in the Crash Course

## Installation (Ubuntu)

Set our user to run the Docker without sudo:

`$ sudo usermod -aG docker $(whoami)`

Check if Docker is somehow installed and where it's installed:

`$ docker info`

## Working with Images

Running a basic image test:

`$ docker run hello-world`

List available images from Dockerhub: (Using Ubuntu as example)

`$ docker search ubuntu`

Pulling image from Dockerhub:

`$ docker pull ubuntu`

Check all images available on the system:

`$ docker images`

Information about the container:

`$ docker inspect ubuntu`

Running the pulled image as a container:

`$ docker run ubuntu`

Check all running containers:

`$ docker ps -a`

If there's a container that is running and you want to stop it:

`$ docker rm ubuntu`

Running the container with an interactive mode and remove it after running:

`$ docker run --rm -it ubuntu`

Delete dangling images (images that are not being used, usually the ones that haven't any tag associated to it):

`$ docker system prune`

## Dockerfile Example

Create a raw file called `Dockerfile`:

```
FROM ubuntu:latest  
RUN apt-get update   
    && apt-get install --no-install-recommends --no-install-suggests -y curl 
    && rm -rf /var/lib/apt/lists/*
ENV SITE_URL http://example.com/  
WORKDIR /data  
VOLUME /data  
CMD sh -c "curl -Lk $SITE_URL > /data/results" 
```

One has to build on the same directory where the Dockerfile is located, we give the `-t` argument to denote the tag of our image:

`$ docker build -t our-first-dockercontainer .`

Running the container:

`$ docker run --rm our-first-dockercontainer`

Running the container but mapping the output to our local OS:

`$ docker run --rm -v $(pwd)/vol:/data/:rw our-first-dockercontainer`  

To check the results from our container:

`$ cat ./vol/results` 

Passing environment variables to our container:
`$ docker run --rm -e SITE_URL=https://facebook.com/ -v $(pwd)/vol:/data/:rw our-first-dockercontainer`

If we wanted to run a dettached proccess, i.e. after running it we leave the process to be running in the background and we can interact with the container using the current terminal session:

` $ docker run -d -p 8080:80 container_image_name `

## Setting Up Local Development a Breeze Using Docker

Assuming we're running an API using uvicorn and FastAPI:

` $ docker-compose up --build`

Such that in the docker-compose file there will be a reference to the Dockerfile where we create a working directory in the container and this is referenced in the compose command along with the port mapping to the local computer.

## Mounting File/Directories to a Container in Windows

1. Make sure to have HyperV instead of WSL.
2. Go to Settings -> Resources -> File Sharing -> Place the path to the folder to be mounted.
3. In my specific case I wanted to pass the GCP credentials, so I had to create an env variable inside the container, hence the -e.
4. The trick was with passing the environment variable from my local, which I have tested by using echo `$env:GOOGLE_APPLICATION_CREDENTIALS`, **but one has to use braces** in order to pass it correctly to the command argument.
5. The problem was that every time you pass a relative or a wrong path to the docker volume parameter, Docker in Windows (specifically) will mount it as a folder, even if it doesn't exists, so what you end up in the container is a folder, not the json file that I was expecting.

The command to pass the credentials from local to the container is as follows:

```$ docker run --rm -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/credentials2.json -v ${env:GOOGLE_APPLICATION_CREDENTIALS}:/tmp/keys/credentials2.json list_bucket_objects```

Notice that -e stands for the environment variable that will be set with the name of GOOGLE_APPLICATION_CREDENTIALS, which is the venv used by google to retrieve
credentials automatically by using ADC.

The code snippet for listing files in a bucket by using GCP can be found [here](https://github.com/hpoleselo/GCP-Helper-Functions/tree/main/gcp_auth_to_docker).
