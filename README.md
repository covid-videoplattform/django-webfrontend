# COVID Videoplatform Django Frontend

This is an appointment management system for jitsi-meet video calls.

It allows you to maintain a list of staff members which can be assigned appointments by date and time.

Each appointment gets a unique jitsi room name that you can then give out to a patient/client.

Regular permanent Jitsi rooms can also be created. (i.e. for regular team calls).

The system assumes you have your own jitsi-meet instance set up. You can in theory use it with public instances, but we recommend using a separate instance because the performance of public instances can vary a lot due to heavy usage.


## development setup

1. install python 3 and django 3

2. install all python dependencies from requirements.txt

3. install the less css compiler (>= 3.11): 
```
npm install -g less
```

### fixtures / pre-seed database
You should run  `python manage.py loaddata pages` to add the initial flatpages for / (home), about, imprint and privacy. You can also run `python manage.py loaddata house` to add some example staff members to your database.


### i18n
If you want to work on translations, make sure gettext is installed on your system, then use 
`python manage.py compilemessages` to create the .po files in the locale folder. And `python manage.py compilemessages` to compile them into a .mo file for django to use.