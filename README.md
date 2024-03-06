# Ice-server

## Problem statement

We have an ice cream company which  has multiple outlets. Every outlet has multiple flavors but there are three mandatory flavors: chocolate, vanilla and mint. So we have our api  with two routes the first one is the normal outlets and admin route. Normal outlet route allows us to create and delete outlets and admin route has a powerful admin point which can see all outlets can delete an outlet or can add a new one, the admin route uses the basic authentication feature of django. [All of this is wrapped into a docker container]

## How to install and use

Then using command line go into the folder and use docker compose up --build

Make sure to create a django admin for future use-  python manage.py createsuperuser

username:- admin Password:- 123456

Then use postman or any other similar tool to run get post and delete commands mentioned below and make sure Basic Authentication is on in the Authorization tab

-> Get 
http://0.0.0.0:8000/api/outlets
http://0.0.0.0:8000/api/admin/outlets

To get specific outlet
http://0.0.0.0:8000/api/outlets/outletID/
http://0.0.0.0:8000/api/admin/outletID/

-> Post
http://0.0.0.0:8000/api/outlets/
http://0.0.0.0:8000/api/admin/outlets/

Use this is body raw as input
{
    "name": "Example Outlet",
    "password": "examplepassword",
    "location": "Example Location",
    "number_of_employees": 5,
    "flavors": "Example Flavor"
}


-> Delete

http://0.0.0.0:8000/api/outlets/outletID/
http://0.0.0.0:8000/api/admin/outletID/
