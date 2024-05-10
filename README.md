# Terminal App

## Repository
[Ghithub Terminal App 2024](https://github.com/nlina-0/terminal-app-2024)

## Style Guide
[PEP 8](https://peps.python.org/pep-0008/)

## Features

A terminal application that tracks user vitamins/supplement intake.

### 1. User signin and login

- At the starting menu the user is given 3 options, signup, login and exit.
    - Signup: User creates account, enters name and age.
    - Login: If user has existing account, user can login using name.

- Stores user account information in .csv (user name and age)

### 2. Vitamin/supplement tracker
- User selects vitamin from list to track
- User is given recommended daily intake based on age
- Terminal asks if user takes any supplements, if yes, user is asked to enter supplment intake and the data is stored into .csv
- The app will inform if the user has met their daily recommended intake.
    - If the same vitamin is recorded more than once within a day, the user will be asked if they want to overwrite existing data.

### 3. View history
- User can view dated history of vitamin intake
- The app will read through user_data.csv and only return the data of current user


## Installation Guide

Input following code into command line.
```bash
./src/run_app.sh
```
- The script will create virtual enviornment and install required dependencies. 

#### Dependencies
- colorama

#### System Requirements

This application requires Python 3.10 to be installed. Check what version of Python you currently have installed by running the following command:
```bash
python --version
```

<!-- ## Referenced Source -->