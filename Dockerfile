# narenm/dev-env is based on ubuntu:16.04
# Git location of dev-env
#   - https://github.com/naren-m/Dockerfiles/tree/master/dev-env
FROM narenm/dev-env
MAINTAINER Naren Mudivarthy <narenuday595@gmail.com>

ENV PYTHON_VERSION 2.7
ENV NUM_CORES 4

# Install OpenCV 3.1.0
RUN apt-get -y update
RUN apt-get -y install python$PYTHON_VERSION-dev wget unzip \
               build-essential cmake git pkg-config libatlas-base-dev \
               gfortran \
               libjasper-dev libgtk2.0-dev libavcodec-dev libavformat-dev \
               libswscale-dev libjpeg-dev libpng-dev libtiff-dev 

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm get-pip.py

WORKDIR /webapp 
# Add requirements.txt
ADD requirements.txt /webapp
 
# Install uwsgi Python web server
# RUN pip install uwsgi

# Install app requirements
RUN pip install -r requirements.txt
 
# Create app directory
ADD . /webapp
 
# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp
 
# Expose port 8000 for uwsgi
EXPOSE 8000
