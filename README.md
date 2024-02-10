Instruction:
after downloaded the zip file and extraction it, at command promt (recommended) or the ide your using, navigate to the directory that you just extract just now.
Activate Your Virtual Environment (Optional but recommended):

you can continue by:
  
**To start the program**

Step 1: typing _python -m venv venv_ in cmd

Step 2: then type venv\Scripts\activate

Step 3: you need to install all the pip which are:
-------------------------------------------
        - Django  (needed)
        - django-jazzmin (needed)
        - pillow (needed)

-------------------------------------------

<br/>Ignore this for now
- sqlparse (standby)
- tzdata (standby)
- asgiref (standby)
------------------------------------------
**By typing pip install (the package name)**

step 4: type _python manage.py makemigrations_

step 5: type _python manage.py migrate_

Step 7: type _python manage.py runserver_

Step 8: then when to your browser then seaerch for _127.0.0.1:8000_


<br/><br/><br/><br/><br/><br/>

**Extra:**<br/>
* You can deactivate your virtual enviroment by typing _deactivate_
<br/><br/>
* You can create admin(superuser) by typing **python manage.py createsuperadmin** and fill in the detail requested
<br/><br/>
* For Employee, admin need to register at website first, then change the role manually to Employee
<br/><br/>
* If you want to update the admin logout, change the file by nagivate to \venv\Lib\site-packages\jazzmin\templates\admin...... find the base.html then replace it
<br/><br/>
* For admin to generate report, type in the address after login into **the admin account first** [127.0.0.1:8000/AllUsers/generatecsv](http://127.0.0.1:8000/AllUsers/generatecsv/) in the browser

<br/><br/><br/><br/>

**Extra's extra**<br/><br/>
<font size="25">**Resident POV**</font><br/>
**Notice Board**
- User can view the announcement updated by the admin
- User can search the announcement by title
- User can search the announcement by month also


**Manage Profile**
- User can view their parking lot and house unit but unable to change it
- User can manage their profile (username, email etc)
- User can also change the password (It will redirect to the other page)


**Bill Payment**
- User can view their outstanding amount
- Inovice will be shown to the user, user can als choose to download it
- User need to upload the proof of payment when submitting


**Feedback**
- Users can provide feedback and also upload pictures to accompany their complaints

  
**Logout**
- User will be logged out

  
<br/><br/><br/><br/>

<font size="25">**Visitor POV**</font><br/>
- Users need to fill out the form before entering the residential area
- Users can provide feedback and also upload pictures to accompany their complaints

<br/><br/><br/><br/>

<font size="25">**Employee POV**</font><br/>
**Notice Board**
- User can view the announcement updated by the admin
- User can search the announcement by title
- User can search the announcement by month also

**Manage Profile**
- User can manage their profile (username, email etc)
- User can also change the password (It will redirect to the other page)

**View Timetable**
- User can view their working schedule

<br/><br/><br/><br/>

<font size="25">**Administration POV**</font><br/>
**CustumUser**
- Admin can manage the user profile including their role, username, email, parking lot, house unit etc....

**Payment**
- Admin can maanage the invoice and to seletect where is the user have paid the excessive amount or not

**Paymebnt Upload**
- Admins can check the payment proofs submitted by residents

**EmployeeSchedule**
- Admin can upload the employee's working schedule

**Feedback**
- Admin can check for the feedback and feedback image

**NoticeBoard**
- Admin can upload the announcement

**Generate Report**
- Type [127.0.0.1:8000/AllUsers/generatecsv](http://127.0.0.1:8000/AllUsers/generatecsv/) at your browser to view the report tab

**Visitor**
- Admin can check for the visitor record



                                                                                                                                                        
