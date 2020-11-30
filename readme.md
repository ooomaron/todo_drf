# To-Do App using Django Rest Framework

Simple API built with DRF.

## Functions implemented

- *CRUD system*  
- *Deadline for each task*  
- *Expired tasks*  

## Required installations 
```
pip install python
pip install django
pip install djangorestframework 
```

## Usage

```python
django-admin startproject projectname
django-admin startapp appname
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver 
```

## API Endpoints
```
Api Overview:   /api/                         
List:           /api/task-list/                     # displays lists in descending order
Detail View:    /api/task-detail/<str:pk>/          # view the details
Create:         /api/task-create/                   # create a new task
Update:         /api/task-update/<str:pk>/          # update a task
Delete:         /api/task-delete/<str:pk>/          # delete a task
```
