

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
 
This will install all the dependencies from `requirements.txt`  and run migrations and Django server ***automatically***

To stop the container `docker-compose stop`

Web server will be running at `http://0.0.0.0:8000/`

## Debug

Follow [https://docs.docker.com/compose/django/](https://docs.docker.com/compose/django/)


## API Doc
 
 HOST - http://0.0.0.0:8000
 
 ##### List all customers
 

	GET /customers
    Status 200  OK
    
    Response JSON
    
    [{
        "id": 1,
        "name": "gurjot",
        "phone_number": "855",
        "address": null
    },
    {
        "id": 2,
        "name": "john",
        "phone_number": "855",
        "address": null
    }]

##### Create new customer

    POST /customers
    
    Status 201  Created
    
    Params JSON
    
    {
    "name": "john",
	"phone_number": "855",
	"address": "125 Berlin"
	}
    
 ##### List all orders

    GET /orders
    
    Status 200  OK
    
    Response JSON
    
    [
    {
        "id": 1,
        "order_items": [
            {
                "id": 1,
                "pizza_flavour": "Marinara",
                "pizza_size": "Large",
                "quantity": "10000",
                "order": 1
            }
        ],
        "order_status": "Pending",
        "customer": 1
    },
    {
        "id": 2,
        "order_items": [
            {
                "id": 2,
                "pizza_flavour": "Marinara",
                "pizza_size": "Large",
                "quantity": "10000",
                "order": 2
            }
        ],
        "order_status": "Pending",
        "customer": 1
    }]

##### Create new order

    POST /orders
    
    Status 201  Created
    
    Params - JSON 
    
    {
    "order_items": [
        {
            "pizza_flavour": "Salami",
            "pizza_size": "Large",
            "quantity": "2"
        },
        {
            "pizza_flavour": "Marinara",
            "pizza_size": "Small",
            "quantity": "3"
        },
        {
            "pizza_flavour": "Margarita",
            "pizza_size": "Medium",
            "quantity": "10"
        }
    ],
    "customer": 1,
    "order_status": "Pending" 
    }


   
   
   
   ##### Update existing order
   
	PUT /orders/<order_id>/
	
	Status 200  OK
	
	Params JSON 
	(provide order item id you want to update, here in case 9)
	
    {
    "order_items": [
        {
            "id": 9,
            "pizza_flavour": "Salami",
            "pizza_size": "Large",
            "quantity": "2"
        }
    ],
    "customer": 1,
    "order_status": "Delivered"
    }

##### Delete existing order

    DELETE /orders/<order_id>/
    
    Status 204  No Content

##### Filter  orders based on order status or customer id

    GET /orders?order_status=Delivered&customer=1
    
    Status 200  OK
    
    Response JSON
    
    [{
        "id": 9,
        "order_items": [
            {
                "id": 11,
                "pizza_flavour": "Salami",
                "pizza_size": "Large",
                "quantity": "2",
                "order": 9
            }
        ],
        "order_status": "Delivered",
        "customer": 1
    }]


