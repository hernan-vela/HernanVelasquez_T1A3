#!/bin/bash
python3 -m venv virtualenv

# Activation of virtual environment
source virtualenv/bin/activate

#Install the dependencies from requirements.txt
pip install -r requirements.txt

#Run the main application
python3 src/main.py

# Deactivate the virtual environment
deactivate