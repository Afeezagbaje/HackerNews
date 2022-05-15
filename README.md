# Hacker News

Hackernews clone that sync with the hackernews website



## Technologies

- [Python 3.9](https://python.org): Base programming language for development
- [Django Framework](https://www.djangoproject.com/): Development framework used for the application
- [Celery](https://github.com/celery/celery): A simple, flexible, and reliable distributed system to process vast amounts of tasks
- [Django Celery Beat](https://github.com/celery/django-celery-beat): A Database Period task scheduler
- [Redis](https://github.com/redis/redis-py): A NoSQL Database that serves as a Celery Broker and Result Backend
- [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment

## How To Start App

- Clone the Repository
```
git clone https://github.com/Afeezagbaje/HackerNews.git
```
- Then run the following commands consecutively
```
python3 -m venv venv 
```
- To activate virtual environment (MacOS users): 
```
source venv/bin/activate
```
- To activate virtual environment (Windows users):
```
source venv/Source/activate
```
- Install dependencies as follows (both MacOS & Windows):
```
pip3 install -r requirements.txt
```
- Make migrations by running the commands below in succession:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```
- Make sure redis is running on your local machine:
- Start a Celery worker by running:
```
celery -A config.celery worker -l info
```
- Start a Celery beat by running:
```
celery -A config.celery beat -l info
```


- Running the above command will Start up the following Servers:
    - Django Development Server --> http://localhost:8000
    - Redis Server --> http://localhost:6379

## Exploring The App

Make sure that all the above servers are running before you start exploring the project. If those servers are up and running, have fun with the app!!!

### HackerNews App

You can explore the Hackernews App by going to `http://localhost:8000` on your browser. You will be able to see the following features

1. View list of paginated latest hackersnews
2. Filter hackernews by type: `story`, `job` and `poll`
3. Search hackernews by text
8. Login to Django Admin on `http://localhost:8000/admin`

### API

You can explore the Hackernews App by going to `http://localhost:8000` on your browser. The following endpoints are accessible

1. GET Stories --> `http://localhost:8000`
2. GET Filtered news by type
   1. For story --> http://localhost:8000/?f=story
   2. For poll --> http://localhost:8000/?f=poll
   3. For job --> http://localhost:8000/?f=job
3. GET Story Details --> http://localhost:8000/<str:pk>/
4. Search news --> http://localhost:8000/?q=<str:query>

