# Terminal App

## Repository
[Ghithub Terminal App 2024](https://github.com/nlina-0/terminal-app-2024)

## Style Guide
[PEP 8](https://peps.python.org/pep-0008/)

## Features

A terminal application that tracks user vitamins/supplement intake.

### 1. User signin and login
Starts with menu 1, the user is given 3 options, signup, login and exit. 

- **Signup**: User creates account, enters name and age.
    - Stores new user account information into user_acc.csv (user name and age).
- **Login**: If user has existing account, user can login using name.
- **Exit**: Terminates the program.

The options will be looped over if the user does not choose valid option. 

### 2. Vitamin/supplement tracker
User is presented with menu 2. The options are to track vitamin, view history or exit program. If an invalid choice is entered the menu will loop over.
- User is given a list of vitamins to choose from.
- User is given recommended daily intake based on age when vitamin is selected.
- User is asked if they take any supplements:
    - If yes, user is asked to enter supplment intake and the data is stored into user_data.csv.
    - If no, nothing will be recorded.
- The app will inform the user if they have met their daily recommended intake.
- Once this is complete, the user will be taken back to menu 2. 

Data recorded for the same vitamin more than once on the same day will be overwritten or omitted. The user will have an option to overwrite. 

### 3. View history
- User can view dated history of vitamin intake, supplement amount and recommended intake.
- The app will read through user_data.csv and only return the data of current user.  
- The user can press enter to continue back to menu 2. 
<br />

## Development Plan

## Installation Guide
1. Change directory into **/src** folder.
2. Input following code into command line:
```bash
./run_app.sh
```
The script will:
1. Check to see if you have Python3 and pip3 are installed. If not, a link will be provided to follow through with. For manual installation, please look below to system requirements.
2. Create virtual enviornment.
3. Install required dependencies. 
4. Run the application in terminal.

#### Dependencies
- colorama

#### System Requirements
**Python 3** is needed to run this application. To check if you have Python3 installed or to check what version you have, input the following command:
```bash
python --version
```
- To install Python, check out https://installpython3.com/

**Pip3** is needed to run this application. To see if you have pip3 installed, input the following command:
```bash
pip --version
```
- To install pip3, check out https://pypi.org/project/pip/

<!-- ## Referenced Source -->