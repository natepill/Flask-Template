# Prerequisites
* Installed Git, git initialized in local project, committed, and pushed to remote git repository
* Installed Heroku CLI and logged in to Heroku account (if needed)
* Installed Virtual ENV
* Installed latest version of pip (pip3)



# Deployment Instructions From Your Project's Root Directory
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
* heroku ps:scale web=1
* heroku open





# Notes
* Heroku Dev Center's Guide on Deployment: https://devcenter.heroku.com/articles/getting-started-with-python
* Some commands have already been run in order to deploy a basic flask app
* Used 'pip3-freeze > requirements.txt' on personal project so there may be unnecessary requirements in requirements.txt for your project
* link to app: https://protected-island-49632.herokuapp.com/
