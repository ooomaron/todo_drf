# To Do App using Django Rest Framework

## Functions implemented

- *CRUD system*  
- *Deadline for each task*  
- *Open/Expired tasks*  
## Description

Simple API to create and manage tasks. Each user can keep track of their own tasks and mark them as complete when they are finished. The user able to edit the `title`, whether it is `complete` and `deadline` of the tasks and delete them. The admin can create users.

# Model Task
| Name      | Type          | Description            |
|-----------|---------------|------------------------|
| title     | CharField     | Title of the task      |  
| completed | BooleanField  | Completed or not       |          
| created   | DateTimeField | Task created time      |   
| deadline  | DateTimeField | Set deadline of a task |   
| author    | ForeignKey    | Django User            |  


> Task Model also has `status` property that is set to either `open` (till deadline) or `expired` (if deadline is passed) 

---
# Installation process
## Install the system dependencies
 * git
 * pip
  
## Get the code from
 - Clone the repo `git clone https://github.com/ooomaron/todo_drf.git`

## Required dependencies 
```python
pip install -r requirements.txt
```
## Generate the database

```python
python manage.py migrate 
```
## Run the server

```python
python manage.py runserver 
```
 Server runs at http://127.0.0.1:8000/

---

## Authentification 
To make the requests to the API endpoints need an Authorization header with a valid token 
```
Authorization: Token <token>
```
To get a token it's necessary to send a request `POST /api-token-auth/` with username and password in JSON format. New users are created using Django admin panel.
## API Endpoints

| Overview      | Endpoints                     | Description            | Methods |
|---------------|-------------------------------|------------------------|---------|
| User Token    | /api-token-auth/              | obtain token for user  | POST    |   
| Task List     | /api/task-list/               | displays tasks in      | GET     |  
| Open Tasks    | /api/task-list?status=open    | displays open tasks    | GET     |  
| Expired Tasks | /api/task-list?status=expired | displays expired tasks | GET     |  
| Detail View   | /api/task-detail/<str:pk>/    | view the task details  | GET     |          
| Create        | /api/task-create/             | create a new task      | POST    |   
| Update        | /api/task-update/<str:pk>/    | update a task          | PUT     |   
| Delete        | /api/task-delete/<str:pk>/    | delete a task          | DELETE  |   


