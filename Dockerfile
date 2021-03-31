FROM python:3.8-slim-buster

WORKDIR /ourAppData

VOLUME /ourAppData

# Copy the requirements.txt file to our Docker image
COPY requirements.txt .

# Normalmente roda em buildtime
RUN pip3 install -r requirements.txt

# Environment variable to be passed
ENV WEBSITE_URL google.com

# Adding the Python program to the Docker image, since we're already in /data we use dot as the target directory for copying
COPY webpage-request.py .

# CMD e ENTRYPOINT  sao overridable on the command-line 
# Já que estamos buildando do docker-compose, damos o comando por lá
#CMD python webpage-request.py ${WEBSITE_URL}
