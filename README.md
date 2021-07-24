# GHETTO WATCH 

#### Created on 24 July 2021
#### By Samuel Maingi Mutunga

---
# Description  
Have Created a WebApp that allows one to be in the loop about everything happening in one's neighbourhood. It has A section for post where the latest happenings are posted. It has contact information for Police and health services 

---
## User Stories  
User Can :-

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

---
## Access the website
Need the latest browser to be able to View

Follow this link 

It is hosted by heroku

---

## Setup and Installation  
To get the project .......  
  
##### Clone Repository:  
 ```bash 
https://github.com/layersony/ghettowatch.git
```
##### Install and activate Virtual Enviroment envgallery  
 ```bash 
cd awwwards  && python3 -m venv envghetto && source envghetto/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  

  Create .env file
```bash
  SECRET_KEY='<SECRET_KEY>'
  DEBUG=True 
  DB_NAME='database name'
  DB_USER='database user'
  DB_PASSWORD='password'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1

  EMAIL_USE_TLS=True
  EMAIL_HOST='smtp.gmail.com'
  EMAIL_PORT=587
  EMAIL_HOST_USER='email'
  EMAIL_HOST_PASSWORD='email-password'
```

 ```bash 
python manage.py makemigrations ghetto 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py server 
```
##### Test Application  
 ```bash 
 python manage.py test ghetto
```
Open the application on your browser `127.0.0.1:8000`.  
  
### Access Django Admin
```bash
>>> Username: layersony
>>> Password: < Buy me Coffee >
```
## Technology used  
  
* HTML, CSS, Bootstrap

* Git

* Pythonp, Django Framework, Rest_framework

* Heroku 
  
  
## Bugs  
* None at the Moment
  
## Contact Details
sammaingi5@gmail.com

@code_with_maingi (Twitter)

@Maingi `Slack Moringa`

---

### License
This Project is under the [MIT](LICENSE) license

Copyright (c) 2021 MaingiSamuel