# Plex Dashboard
A dashboard for Plex related services -- using Django
    * could be used for other things too.

Still in development. I would consider this beta stage. Everything works, but there are
 improvements to be made. More to come!
 
 I'm still testing the fixtures!
 
#### Python Version
    - v2.7
    - Need to test against v3
    
#### Django Version
    - v1.10.3
    
#### OS Versions
    - MacOS
    - Windows 10 (Windows 7 should work)
 

Everything is working. Some cleanup is needed. 
## Here's the TODO list.
   1. ~~Clean database~~
        - ~~create fixtures~~
        - create commands/scripts for running fixures
        - ~~gitignore db~~
   2. Create update mechanism
   3. organize plex_dashboard.css
   4. Testing with different operating systems and versions
        - Successfully test against Mac and Windows
   5. Create update mechanism
   6. maybe create installers with [pyinstaller](http://www.pyinstaller.org/), or stick with git
   7. ~~Instructions for getting started.~~
   8. Get logging working properly
   9. Service status on home page
   
## Changes since last commit.
   1. Updated fixtures
   2. removed the db
   3. Removed django-toolbar
   4. Added Install_instructions.md
   
## Default Credentials
Be sure to change at least the password. There are password restrictions listed (django defautl).
### username
   - admin
   
### Password:
   - ChangeMe11!!
   
![What is looks like](http://i.imgur.com/jCHWMo6.png)

![The menu](http://i.imgur.com/PODI342.png)

![The settings](http://i.imgur.com/QdgBj2M.png)


