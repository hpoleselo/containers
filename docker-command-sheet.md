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