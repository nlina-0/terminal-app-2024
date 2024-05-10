# Terminal App

## Repository
[Ghithub Terminal App 2024](https://github.com/nlina-0/terminal-app-2024)

## Style Guide
[PEP 8](https://peps.python.org/pep-0008/)

<!-- ## Referenced Source -->

## Features

A terminal application that tracks user vitamins/supplement intake.

1. User signin and login
    - stores user account information in .csv (user name and age)
    - user is given 3 options, signup, login and exit
    - signup:
        - user creates account, enters name and age
    - login:
        - if user has existing account, user can login using name

2. Vitamin/supplement intake
    - User selects vitamin from list to track
    - User is given recommended daily intake based on age
    - Terminal asks if user takes any supplements, if yes, use is asked to enter supplment intake and the data is stored into .csv
    - The app will inform if the user has met their daily recommended intake.
        - If the same vitamin is recorded more than once within a day, the user will be asked if they want to overwrite existing data.

3. View history
    - user can view dated history of vitamin intake