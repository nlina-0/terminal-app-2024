#!/bin/bash

# if pip3 is installed then continue, if not then 
    # tell user to install pip

# if python is installed then continue, if not then
    # tell user to install python

# python3 -m venv .venv
source .venv/bin/activate
echo "Installing application..."
pip3 install -r ./requirements.txt
python3 main.py
