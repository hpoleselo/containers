FROM python:3.8-slim-buster

# Environment variable to be passed
ENV WEBSITE_URL www.facebook.com

WORKDIR /data

#VOLUME /data
# HEkki

# Copy the requirements.txt file to our Docker image
COPY requirements.txt .

# Normalmente roda em buildtime
RUN pip3 install -r requirements.txt

# Adding the Python program to the Docker image, since we're already in /data we use dot as the target directory for copying
COPY webpage-request.py .

# CMD e ENTRYPOINT  sao overridable on the command-line 
#CMD ["python", "webpage-request.py", "echo ${WEBSITE_URL}"]
CMD python webpage-request.py ${WEBSITE_URL}