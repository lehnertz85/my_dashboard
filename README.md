# Plex Dashboard
A dashboard for Plex related services -- using Django
    * could be used for other things too.

Still in development. I would consider this beta stage. Everything works, but there are
 improvements to be made. More to come!

Everything is working. Some cleanup is needed. 
## Here's the TODO list.
   1. Clean database
        - create fixtures
        - create commands/scripts for running fixures
        - gitignore db
   2. Create update mechanism
   3. organize plex_dashboard.css
   4. Testing with different operating systems
   5. Create update mechanism
   6. maybe create installers with [pyinstaller](http://www.pyinstaller.org/), or stick with git
   7. Instructions for getting started.
   8. Get logging working properly
   
## Changes since last commit.
   1. Incorporated permission's and auth
        - login page
        - profile page (password reset)
        - Multiple user's can login
            * use the django admin console to add new users
   2. Added form error messages
   3. code cleanup and bug fixes
   4. Ran migrations after changing an attribute
   5. prep for versioning
        - created a changelog file
   6. removed unused code and files
   7. Probably more that I have forgotten
   
## Default Credentials
Be sure to change at least the password. There are password restrictions listed (django defautl).
### username
   - admin
   
### Password:
   - ChangeMe11!!
   
![What is looks like](http://i.imgur.com/jCHWMo6.png)

![The menu](http://i.imgur.com/PODI342.png)

![The settings](http://i.imgur.com/QdgBj2M.png)


