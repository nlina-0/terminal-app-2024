#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python3, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
elif ! [[ -x "$(command -v pip3)" ]]
then
  echo 'Error: 
    Pip3 is needed to install dependencies, but it looks like Pip is not installed.
    To install pip3, check out https://pypi.org/project/pip/' >&2
  exit 1
fi
python3 -m venv .venv
source .venv/bin/activate
echo "Installing application..."
pip3 install -r requirements.txt
python3 main.py 
