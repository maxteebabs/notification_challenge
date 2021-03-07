## SWVL NOTIFICATION APP
----

## Introduction
The Capstone project is a project that communicates with our customers via notifications. It allows sending
Promo codes and riders notification to customers via SMS


## Motivation
In search for new opportunites, I am inpired to take on this backend challenge.


## Getting Started
### Installing Dependencies
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Docker
Follow instructions to install the latest version of docker for your platform in the [docker docs](https://docs.docker.com/install/)
After Installation is complete, run:
```bash
docker build -t swvl .
docker-compose build 
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [DOCKER] help developers and development teams build and ship apps with ease. Docker allows you to build and share containerized applications and microservices. 

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension I used for cross origin request



## Starting the App
### To run the migration script
```bash
docker-compose exec api python manage.py db init
```
```bash
docker-compose exec api python manage.py db migrate
```
```bash
docker-compose exec python manage.py db upgrade
```

### To start the application, run
```bash
docker-compose build
```

```bash
# docker run --env-file=.env -p 5000:5000 swvl
docker-compose up -d
# docker-compose exec db psql --username=postgres --dbname=swvl
```

### How to run test
```bash
# python manage.py test
docker-compose exec api python manage.py test
```
<!-- OR
```bash
python -m unittest discover 
``` -->

## API Endpoints

### GET '/api/notifications'
* fetches a collection of all notifications in the database
```
curl --location --request GET 'localhost:5000/api/notifications'
```
Sample Response:
```
{
    "notifications": [
        {
            "channel": "sms",
            "created_at": "Sat, 06 Mar 2021 15:34:38 GMT",
            "group_name": null,
            "id": 28,
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "status": "sent",
            "type": "single",
            "user": {
                "id": 1,
                "language": "en",
                "mobile": "23480000000523",
                "name": "Mark Dean"
            }
        }
    ],
    "status": true
}
```

### GET '/api/notifications/1'
* fetches a collection of all notifications per customer_id in the database
```
curl --location --request GET 'localhost:5000/api/notifications/customer/1'
```

Sample Response:

```
"notifications": [
        {
            "channel": "sms",
            "created_at": "Sat, 06 Mar 2021 15:34:38 GMT",
            "group_name": null,
            "id": 28,
            "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
            "status": "sent",
            "type": "single",
            "user": {
                "id": 1,
                "language": "en",
                "mobile": "23480000000523",
                "name": "Mark Dean"
            }
        }
    ],
    "status": true
```

### POST '/api/notifications/send'
* send notification to customers
```
curl --location --request POST 'localhost:5000/api/notifications/send' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
    "should_send_sms": true,
    "should_send_push_notification": false,
    "should_send_email": false,
    "customer_id": 1
}'
```
Sample Response

```
{
    "message": "sent",
    "status": true
}
```

### POST '/api/notifications/group/send'
* send notification to a group of customers
```
curl --location --request POST 'localhost:5000/api/notifications/group/send' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
    "should_send_sms": true,
    "should_send_push_notification": false,
    "should_send_email": false,
    "group_id": 1
}'
```
Sample Response

```
{
    "message": "sent",
    "status": true
}
```

### POST '/api/notifications/riders'
* send notification to riders
```
curl --location --request POST 'localhost:5000/api/notifications/riders' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message": "Dear Customer, Your promo code is xx339kk. Best Regards",
    "should_send_sms": true,
    "should_send_push_notification": false,
    "should_send_email": false,
    "user_id": 1
}'
```
Sample Response

```
{
    "message": "sent",
    "status": true
}
```


