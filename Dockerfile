FROM atul/ubuntu:version1

#RUN apt-get update
# RUN apt-get -y upgrade
 
#RUN apt-get install -y python-dev python-pip

# Add requirements.txt
ADD requirements.txt .
 
# Install uwsgi Python web server
RUN pip install uwsgi
# Install app requirements
RUN pip install -r requirements.txt
 
# Create app directory
ADD . /webapp
 
# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp
 
 
 
# Expose port 3000 for uwsgi
EXPOSE 3000
 
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:3000", "--module", "app:app", "--processes", "1", "--threads", "8"]
