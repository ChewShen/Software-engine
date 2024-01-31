Instruction:
after downloaded the zip file and extraction it, at command promt (recommended) or the ide your using, navigate to the directory that you just extract just now.
Activate Your Virtual Environment (Optional but recommended):

you can continue by:
**1.drag and drop the venv file i gave into folder you extract just now (or directory)**
- 1.1 type .\venv\Scripts\activate in cmd
- 1.2 intall djago-jazzmin by typing _pip install django-jazzmin_
- 1.3 then type _python manage.py runserver_
- 1.4 then when to your browser then seaerch for _127.0.0.1:8000_
- done

  
**2. When ever you encounting any problem, you can do it manually by**
- 2.1 typing _python -m venv venv_ in cmd
- 2.2 then type .\venv\Scripts\activate
- 2.3 you need to install all te pip which are:
      asgiref
      Django
      django-jazzmin
      pillow
      sqlparse
      tzdata

  by typing pip instal (the package name)
  
- 2.4 type _python manage.py runsevrver_
- 2.5 then when to your browser then seaerch for _127.0.0.1:8000_




extra: you can deactivate your virtual enviroment by typing _deactivate_
