# Install instructions

## Walk through
    - These instructions should be fine for Window, MacOS, and other Unix variants.
    - Please read through the whole page before actually installing. There are some key notes.

1. Install python 2.7 or 3.X if not already installed
2. Install pip, if not already installed
3. Make sure python and pip are in your path
3. [clone](https://github.com/lehnertz85/my_dashboard/) or [download](https://github.com/lehnertz85/my_dashboard/releases) the repo from gituhub
4. cd into the folder where manage.py is located

NOTE: You can use virtualenv if you want, or just install the requirements anyways.

5. Run pip install -r requirements.txt to install the requirements (You may have to use sudo)
6. Get the database setup with defaults:
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py loaddata contenttypes admin auth dashboard sessions
  - sudo python manage.py collectstatic (You may have to use sudo)

7. Start the server:
  - You could use nginx or apache (more about web serving can be found [here](https://github.com/lehnertz85/my_dashboard/wiki/Web-servers))
  - or, just run python manage.py runserver 0.0.0.0:8000
      * You can specify any port. It doesn't have to be 8000
  - or, uwsgi --http :8000 --module my_dashboard.wsgi if you are using MacOS or linux
8. Navigate to localhost:8000
9. Enjoy!


If you would like to run this site as public facing (i.e. can access it from work)
you will need to add the hostname or IP to the ALLOWED_HOST section of
/my_dashboard/settings.py and maybe some DNS stuff. If you choose to go public, please read the [Web Servers](https://github.com/lehnertz85/my_dashboard/wiki/Web-servers) wiki for details.

#### EXAMPLE:

    ALLOWED_HOSTS = {
      'REPLACE_WITH_HOSTNAME_OR_IP',
    }