# Pizza Ordering Service!

Docker  19.03.5

Python 3.7.0

Django 2.2.7

psql (PostgreSQL) 12.1

## Task

Build a pizza ordering service with [Django Rest Framework](https://www.django-rest-framework.org/) with following features

##### Order Pizza

 1. Specify flavours (**Margarita, Marinara, Salami**),  the number of pizzas and their size (**Small, Medium, Large**) , quantity in an order
 2. Track status of delivery (**Pending, Delivered**)
 3. Should be able to order multiple pizza of multiple flavours in a single order 

##### Update Order

 1. Should be able to update any property of a pizza order ( quantity, flavour , size , delivery status)
 2. Do not allow update if order status is **Delivered**

##### Remove Order 

 1. Remove order with its identifier

##### Retrieve Order

 1. Retrieve a specific order with its identifier

##### List Orders

 1. Allow listing all orders at once
 2. Allow filtering orders based on **customer id**, **delivery status**

## Setup

Install [Docker](https://docs.docker.com/v17.09/engine/installation/)
Install [Docker Compose](https://docs.docker.com/compose/install/)
Check version using `docker --version`

## How to run app 
After setting up docker and docker-compose, go the root directory of this app (where docker compose file is located)

Run test cases `docker-compose run web python manage.py test`

 Then `docker-compose up`

This will install all the dependencies from requirements.txt automatically.

To stop the container `docker-compose stop`


## Debug

Follow [https://docs.docker.com/compose/django/](https://docs.docker.com/compose/django/)

