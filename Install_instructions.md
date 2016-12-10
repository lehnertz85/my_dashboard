# Install instructions

## Walkthrough

1. Install python 2.7, if not already installed
2. Install pip, if not already installed
3. Make sure python and pip are in your path
3. clone or download the repo from gituhub
4. cd into the folder where manage.py is located

NOTE: You can use virtualenv if you want, or just install the requirements anyways.

5. Run pip install -r requirements.txt to install the requirements
6. Get the database setup with defaults:
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py loaddata contenttypes admin auth dashboard sessions

7. Start the server:
  - You could use nginx or apache
  - or, just run ./manage.py runserver 0.0.0.0:8000
      * You can specify any port. It doesn't have to be 8000
8. Navigate to localhost:8000/dashboard/
9. Enjoy!


If you would like to run this site as public facing (i.e. can access it from work)
you will need to add the hostname or IP to the ALLOWED_HOST section of 
/plex_dashboard/settings.py and maybe some DNS stuff

### EXAMPLE:

ALLOWED_HOSTS = {
  'REPLACE_WITH_HOSTNAME_OR_IP',
}