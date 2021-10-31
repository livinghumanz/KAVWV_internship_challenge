# KAVWV internship certification challenge (Django)

## Design and Development of Dashboard for Student.

## Introduction to the challenge:
You will be provided a base template which contains a Form accepting Student Details like below:
- ID Number
- Student Name
- Date of birth
- government id number
- Email address
- class and school of study
- Parent's Details (Name [Father,Mother], mobile number, occupation, etc...)
- ** you can add any additional details as you wish ** 

On submition of form it redirects the user to Dasboard.html page through Django views. all redirection and linking is done, you just need to implement dashboard.html file. 
It is not necessary to Create a model and push the data to the database, there is no harm doing so as this part will not be considered for Scoring.

### What the Dashboard page Should contain
1. It shoud have student profile image ( make use of static image )
2. Details submited through form should be propogated here.

## Challenge setup
1. download the git repo to your local
2. install requirements.txt $python -m pip install -r requirements.txt
3. Assume you are using python3

## How to initial run the project
1. perform **_ Challenge setup _** step
2. run $python manage.py runserver to initiate a server hosting the project in localhost
3. visit http://localhost:8000/ to view the project

## How to complete the challenge
1. perform **_ Challenge setup _** step
2. once code is in local modify templates/dashboard/dashboard.html file for frontend and dashboard/views.py for fetching data's
3. Prepare a code walk-through video along with the project demo and keep the video link ready *(you can use  __Youtube  or Drive__ to share the video )*
4. Create a github repository named **KAVWV_internship_challenge** and upload the code along with walk-through video link.
5. Explain the code, libraries in use along with steps to execute and setup the project in readme.md file
6. Send us the walk-through video link along with git hub repository link over the mail **_Reply to the mail from KAVWV (info.kavwv@gmail.com) with the github link_**

## Project structure
```bash
KAVWV_internship_challenge
├── dashboard
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── [ ] urls.py
│   └── [ ] views.py
├── kavwv_challenge
│   ├── asgi.py
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   │   └── [x]form.css
│   │   ├── images
│   │   └── js
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── templates
│   ├── base.html **_file to create a base layout_**
│   ├── dashboard
│   │   └── [ ] dashboard.html **_Design your dashboard_**
│   └── [x] index.html **_contains form_**
```