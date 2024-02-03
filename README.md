Instruction:
after downloaded the zip file and extraction it, at command promt (recommended) or the ide your using, navigate to the directory that you just extract just now.
Activate Your Virtual Environment (Optional but recommended):

you can continue by:
  
**1. When ever you encounting any problem, you can do it manually by**

Step 1: typing _python -m venv venv_ in cmd

Step 2: then type venv\Scripts\activate

Step 3: you need to install all te pip which are:
      asgiref (standby)
      Django  (needed)
      django-jazzmin (needed)
      pillow (needed)
      sqlparse (standby)
      tzdata (standby)

  by typing pip install (the package name)

step 4: type _python manage.py makemigrations_

step 5: type _python manage.py migrate_

Step 6: type _python manage.py runserver_

Step 7: then when to your browser then seaerch for _127.0.0.1:8000_




extra: you can deactivate your virtual enviroment by typing _deactivate_
