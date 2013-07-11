django-angular-gae-skeleton
=======================

A Skeleton Repo to get you started using Django, Google App Engine and Angular JS

This skeleton is going to use the script.directive to host the template files on the base.html page to remove any ajax calls for templates.

Some things to make note of:

1) Make sure your settings.local.py is setup for your local database settings. Google App Engine doesn't like SQLite so I've used a local mySQL.

2) Make sure you update your app.yaml with your settings.

3) If you haven't used Google App Engine with Django you'll need to collectstatic every time you make a change to your javascript or CSS. (if anyone knows a way around this please... PLEASE let me know)

4) pip install -r deps.txt to get local dependancies. For instance PIL. dev_appserver.py (or devappserver2.py) doesn't come bundled with PIL.