# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ENV DISPLAY = $DISPLAY

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install git -y
RUN apt-get install wget -y

# Chrome Instalation
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

# Check chrome version
RUN echo "Chrome: " && google-chrome --version

# Clone the repo
RUN cd
RUN git clone https://github.com/emirhanbayar/course_assigner.git