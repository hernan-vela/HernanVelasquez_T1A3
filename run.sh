#!/bin/bash
python3 -m venv virtenv

# Activation of virtual environment
source virtenv/bin/activate

# Ensure pip is up-t-date
python3 -m pip install --upgrade pip

#Install the dependencies from requirements.txt
pip install -r requirements.txt

#Run the main application
python3 src/main.py

# Deactivate the virtual environment
deactivate
