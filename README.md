# KSEA_WEB_API

# SETUP
## INSTALLATION SETUP

1. clone the project with the command
```
git clone https://github.com/seongminchoob/KSEA_web_api.git
```
2. cd into the KSEA_web_api folder
```
cd KSEA_web_api
```
3. check you have virtualenv in your computer
```
virtualenv --version
```
if you don't have virtualenv, download with the command
```
sudo pip3 install virtualenv
```
4. create a virtualenv with the command
```
virtualenv venv --python=python3.8
```
5. check you have homebrew on your computer
```
brew --version
```
6. if you do not, download homebrewbrew
- [brew installation link](https://brew.sh/})

7. download postgres on your computer if you don't have postgres
```
brew install postgres
```
8. activate the virtualenv with the command
```
source ./venv/bin/activate
```
8. install dependencies with the command
```
pip install -r requirements.txt
```

## DATABASE SETUP

1. install postgres if you have not previously.
2. Start postgres on your computer.
```
brew services start postgresql
```
3. start postgres with root privileges
```
sudo -u postgres psql
```
4. create new user kseaapiuser with password "welikeksea", and give createDB access.
```
CREATE ROLE kseaapiuser WITH LOGIN PASSWORD 'welikeksea';
ALTER ROLE kseaapiuser CREATEDB;
```
5. quit and log in with the new user.
```
\q
psql postgres -U kseaapiuser
```
6. create database kseadev in local postgres.
```
CREATE DATABASE kseadev;
```
7. now get out of postgres try to run the command 
```
python manage.py runserver --settings=config.settings.local
```
8. if it worked successfully, run the command
```
python manage.py migrate --settings=config.settings.local
```
9. you're all done with SETUPS!!!!


REFERENCES:
https://www.tutorialspoint.com/postgresql/postgresql_create_database.htm
https://medium.com/@viviennediegoencarnacion/getting-started-with-postgresql-on-mac-e6a5f48ee399#:~:text=%60psql%60%20on%20Terminal,postgresql)%20%2C%20then%20run%20psql%20.
https://www.guru99.com/postgresql-create-database.html

#GENERALS
## RUNNING
1. start postgresql server
```
brew services start postgresql
```
2. start virtualenv
```
source ./venv/bin/activate
```
3. run the command
```
python manage.py runserver
```

## FORMATTING

1. Commit messages
- Use [github commit message guideline](https://gist.github.com/develar/273e2eb938792cf5f86451fbac2bcd51) for formatting commit messages.
2. Coding conventions
- We follow [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/) for coding in Python.
- We try to follow conventions listed in the book "Two Scoops of Django".

## CAUTION

- never change the data in the migrations folder.
- never run makemigrations or migrate unless confirmed.

