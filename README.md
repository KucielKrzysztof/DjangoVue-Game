![Rock, Paper, Scissors Game](/backend/static/images/rps.png)

# Welcome to the Rock Paper Scissors Game! This project is a simple web-based implementation of the classic Rock Paper Scissors game with retro design using Vue.js and Django.

## Table of Contents

1. [Technologies](#technologies)
2. [Features](#features)
3. [Screenshots](#screenshots)
4. [How to Run the Project](#how-to-run-the-project)

## Technologies

<h3 align="center">Technologies used:</h3>
<p align="center"> <a href="https://docs.djangoproject.com/en/5.0/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a><a href="https://vuejs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vuejs/vuejs-original-wordmark.svg" alt="vuejs" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a><a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://sass-lang.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg" alt="sass" width="40" height="40"/> </a>  <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> </p>

## Features

- 🎮Play the Rock Paper Scissors game against a computer opponent.
- 🎯 Keep track of your streak points.
- 🏆 Scoreboard
- 📝 Register and log in.
- 🛠️ Submit bug reports or issues through the Bug Report feature.

## Screenshots

### Main page:

![screen1](/backend/static/images/screenshot1.png)

### Scoreboard:

![screen1](/backend/static/images/screenshot2.png)

### Game:

![screen1](/backend/static/images/screenshot5.png)
![screen1](/backend/static/images/screenshot6.png)

### Login page:

![screen1](/backend/static/images/screenshot3.png)

### Register page:

![screen1](/backend/static/images/screenshot4.png)

## How to Run the Project

### 1st Method(STANDARD):

1. Clone the repository:

```bash
git clone https://github.com/KucielKrzysztof/DjangoVue-Game.git
```

2. Navigate to the cloned repository:

```bash
cd DjangoVue-Game
```

3. \*Install and run virtualenv or not (optional)

4. Install Django dependencies:

```bash
pip install -r backend\requirements.txt
```

5. Run the Django development server:

```bash
python backend\manage.py runserver
```

6. In separated terminal, install Vue dependencies:

```bash
cd frontend
npm install
```

7. Run the Vue.js development server:

```bash
npm run serve
```

8. Open your browser and go to [http://localhost:8080/](http://localhost:8080/) to play the game.

`Windows:`

```bash
start http://localhost:8080
```

`MacOS:`

```bash
open http://localhost:8080
```

`Linuks:`

```
xdg-open http://localhost:8080
```

### 2nd Method(FOR DOCKER):

1. Clone the repository:

```bash
git clone https://github.com/KucielKrzysztof/DjangoVue-Game.git
```

2. Navigate to the cloned repository:

```bash
cd DjangoVue-Game
```

3. Change db for docker in settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

4. build with docker

```bash
docker-compose up --build
```

5. In Django's container cli run migrations

```python
python manage.py makemigrations
python manage.py migrate
```

6. Open your browser and go to
   <br>
   [http://localhost:8080/](http://localhost:8080/)

7. If somethign is not working reload django-conatainer(if it turns on too fast it may not connect to the database)
