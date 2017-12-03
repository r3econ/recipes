[![Build Status](https://travis-ci.org/r3econ/recipes.svg?branch=master)](https://travis-ci.org/r3econ/recipes)

# Recipes

Backend API serving food recipes. Built with Python and Django.
An example of a complex backend app serving restful api and a website.

## What's included
- Restful backend api
- Simple website showing food recipes

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
