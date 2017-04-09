# Sample Standalone Django app with pyexcel data import #

Djangoexcel is sample project that illustrates how to execute a standalone Django script without using Django managed commands. Useful for running batch scripts with smaller datasets, where performance is negligible.
 
For illustration purpose project consists of the bare minimum settings required to run Django without the UI. Most of the settings.py entries have been stripped out including, Django admin, sessions, middleware and staticfiles apps. For your own personal projects, you may continue to keep these predefined Django modules and settings, but are not required when running a console based/backend app. 

Django version 1.10

# Installation  #

    $ cd {YOUR_DIRECTORY}
	$ Git clone
    $ cd djangoexcel
    $ virtualenv venv
    $ source venv/script/activate.sh 
    $ pip install –r requirements.txt 
    $ python manage.py makemigrations sales
    $ python manage.py migrate 
    $ python injester/run.py

To view the contents of the database download [DB Browser for SQLite](http://sqlitebrowser.org/) 


## For more lessons on django [see](https://www.udemy.com/building-your-first-django-app-in-minutes/?couponCode=DIST00001) ##
