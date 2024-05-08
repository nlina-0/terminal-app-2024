# Terminal App

## Repository
[Ghithub Terminal App 2024](https://github.com/nlina-0/terminal-app-2024)

## Style Guide
pep 8

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
    - user selects vitamin from list to track
    - user is given recommended daily intake based on age
    - terminal ask if user takes any supplements, if yes, user enters supplment intake, stored into .csv
    - comparison between recommended intake and supplement intake is made and app records if recommended is met
        - if the same vitamin is recorded more than once within the same day, the latest record will overwrite existing
    - if user is not meeting recommended intake food is recommended to increase vitamin intake (data read from separate file)

3. View history
    - user can view dated history of vitamin intake

4. Energy levels