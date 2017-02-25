# My Dashboard
A dashboard for web services using iFrames -- using Django

   * Built with Plex in mind.
   * default services are Plex related. They can be deleted

Still in development. I would consider this beta stage. Everything works, but there are
 improvements to be made. More to come!

 
#### Python Version
    - v2.7
    - Test against 3.5.2
    
#### Django Version
    - v1.10.3
    
#### OS Versions
    - MacOS
    - Lunux (used on Ubuntu)
    - Windows 10 (Windows 7 should work)
 

Everything is working. Some cleanup is needed. 
## Here's the TODO list.
   1. ~~Clean database~~

       - ~~create fixtures~~
       - create commands/scripts for running fixures
       - ~~gitignore db~~
   2. Create update mechanism
   3. organize my_dashboard.css
   4. ~~Testing with different operating systems and versions
        - Successfully test against Mac and Windows~~
   5. maybe create installers with [pyinstaller](http://www.pyinstaller.org/), or stick with git
   6. ~~Instructions for getting started.~~
   7. Get logging working properly
   8. Service status on home page
   9. Create auto start instructions for all OSes.
   
## Changes since last commit.
   1. Rebranded from Plex Dashboard to My Dashboard
   
## Default Credentials
Be sure to change at least the password through the profile menu item. There are password restrictions listed (django defautl).
### username
   - admin
   
### Password:
   - ChangeMe11!!
   
![What is looks like](http://i.imgur.com/Z3EnGtF.png)

![The menu](http://i.imgur.com/cncXKdK.png)

![The settings](http://i.imgur.com/iBIhr7B.png)


