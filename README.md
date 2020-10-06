## django-docker

This first django app is a codealong to
"Understanding Django by Anthony Herbert"

The only difference (so far) is that I'll be using docker to avoid installing dependencies.
This being my first django and my first django-on-docker app it should be fairly simple and serve as a good starting point for future django-docker projects.

To get started, after downloading the files, you'll need to run:

__docker-compose run web python manage.py migrate__

__docker-compose run web python manage.py createsuperuser__

if you have a new migration that needs running, do:

__docker-compose run web python manage.py makemigrations__

then finally just
__docker-compose up__
should get you going. You can visit http://localhost:8000/admin to manage your database and login with the username you created on the createsuperuser step

Links to the tutorials followed to set this up:

[Understanding Django](https://learning.oreilly.com/videos/understanding-django/9781839214547/)
[Docker Django Setup](https://docs.docker.com/compose/django/)