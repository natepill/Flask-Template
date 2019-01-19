# Prerequisites
* Installed Git, git initialized in local project, committed, and pushed to remote git repository
* Installed Heroku CLI and logged in to Heroku account (if needed)
* Installed Virtual ENV
* Installed Pip3



# Deployment Instructions From The Root Directory
## Commands to Run
* virtualenv env
* source env/bin/activate
* pip3 install flask
* pip3 install gunicorn
* touch .gitignore
* echo "env" > .gitignore
* touch Procfile
* echo "web: gunicorn app:app" > Procfile
* heroku create
* git add .
* git commit -m 'Whatever message'
* git push heroku master







# Notes
* Some commands have already been run in order to deploy a basic flask app
* Used 'pip3-freeze > requirements.txt' on personal project so there may be unnecessary requirements in requirements.txt for your project
* link to Heroku: https://protected-island-49632.herokuapp.com/
