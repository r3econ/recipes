[![Build Status](https://travis-ci.org/r3econ/recipes.svg?branch=master)](https://travis-ci.org/r3econ/recipes)
[![CodeFactor](https://www.codefactor.io/repository/github/r3econ/recipes/badge)](https://www.codefactor.io/repository/github/r3econ/recipes)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)

# Recipes

Backend API serving food recipes. Built with Python and [Django Rest Framework](http://www.django-rest-framework.org/).
An example of a backend django app serving restful API.

<p align="center">
<a href="https://imgur.com/HFXsi8S"><img src="https://i.imgur.com/HFXsi8S.png" title="source: imgur.com" /></a>
</p>

## What's included
- Restful backend API
- Simple website showing food recipes
- Swagger schema
- Admin database interface

## Running locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:r3econ/recipes.git
$ cd recipes

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

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
