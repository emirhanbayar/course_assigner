#!/bin/bash

if [[ "$(python3 -V)" =~ "Python 3" ]]
then
    echo "Python 3 is already installed"
else
    echo "Python 3 is not installed"
    echo "Installing Python 3"
    wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
    tar -xvf Python-3.11.1.tgz
    rm Python-3.11.1.tgz
    cd Python-3.11.1
    ./configure
    make
    make test
    sudo make install
    cd ..
    rm -rf Python-3.11.1
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi



pip3 install selenium==4.9.1
pip3 install get-chrome-driver==1.3.10