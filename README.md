# Gram Insta
### 8th Dec. 2021
## Author 
[Maryann Mwikali](https://github.com/Maryan23)
# Description 
This is an application that has Instagram's minimal features like creating a profile, liking pictures, and commenting on other pictures.1.
##  Live Link
https://mwiksgram.herokuapp.com/ 
## Screenshots
<img src="static/Screenshot from 2021-12-08 07-45-30.png">
<img src="static/Screenshot from 2021-12-08 07-45-43.png">

## User Story 
1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

## Setup and Installation 
##### Clone the repository: 
 ```bash
git@github.com:Maryan23/Gram-Insta.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd My-Insta
 - pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual
- source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations photos
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.
## Technology used 
* [Python3.8](https://www.python.org/)
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)
## Known Bugs 
* There are no known bugs
## Support and Contact Information
Incase of any contributions fork the repo and make any substantial changes.
Incase of any ideas,suggestions or complaints feel free to connect with me on mwikali119@gmail.com 

## License
MIT
Copyright (c) 2021 **Gram-Insta**