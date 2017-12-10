[![Build Status](https://travis-ci.org/r3econ/recipes.svg?branch=master)](https://travis-ci.org/r3econ/recipes)
[![CodeFactor](https://www.codefactor.io/repository/github/r3econ/recipes/badge)](https://www.codefactor.io/repository/github/r3econ/recipes)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)
[![saythanks.io](https://img.shields.io/badge/saythanks.io-now-1EAEDB.svg)](https://saythanks.io/to/r3econ)

# Recipes

Backend API serving food recipes. Built with Python and [Django Rest Framework](http://www.django-rest-framework.org/).
An example of a backend django app serving restful API.

<p align="center">
<a href="https://i.imgur.com/Ninptgs.png"><img src="https://i.imgur.com/Ninptgs.png" title="Image" /></a>
</p>

## But what's there?
- Token authentication (sign up, login, logout)
- Custom permissions (e.g. only author of the recipe can modify it)
- Searching and filtering (e.g. searching for recipes by title, description)
- User profiles
- Recipes can be bookmarked

### Extras
- Simple website showing food recipes built using [Bootstrap](https://getbootstrap.com/)
- Swagger schema ([What's Swagger?](https://swagger.io/))
- Admin database interface

## Live demo

Working demo is deployed to heroku and you can check it out here:
- [API root](https://hidden-eyrie-76546.herokuapp.com/api/) shows all the endpoints using Swagger
- [Simple website](https://hidden-eyrie-76546.herokuapp.com/)
- [Admin interface](https://hidden-eyrie-76546.herokuapp.com/admin/)

Authenticate with a demo user:
```
username: bob
password: bob123bob
```

## Upcoming
I'm working on adding the following features:
- Image upload for recipe images and user profile pictures
- Simple webpage showing recipe details
- Increasing test coverage

## Running locally

Make sure you have Python 3 [installed properly](http://install.python-guide.org).  Also, install [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

Clone the repo
```sh
$ git clone git@github.com:r3econ/recipes.git
$ cd recipes
```

Create virtual environment with Python 3 and activate it
```
virtualenv -p python3 env
. ./env/bin/activate
```

Install dependencies
```
$ pip install -r requirements.txt
```

Prepare the database
```
$ python manage.py migrate
```

Start the development server
```
$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
