#!/bin/bash          

# Create the virtualenv and install its requirements

VENV=$1
REQS_FILE="requirements.txt"

# Install pip, virtualenv and virtualenvwrapper
sudo apt-get install python-pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper

# Read the virtualenvwrapper script
source `which virtualenvwrapper_lazy.sh`

#virtualenv $VENV
#source $VENV/bin/activate
mkvirtualenv $VENV
workon $VENV
 
#echo "In virtualenv directory"
#cd $VENV

pip install -Ur $REQS_FILE





