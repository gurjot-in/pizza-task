# Pizza Ordering Service!

Docker  19.03.5

Python 3.7.0

Django 2.2.7

psql (PostgreSQL) 12.1


# Setup

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

