# Chatbot-backend

Api that connects to a chatbot to register users and send a welcome email.
It also connects to a costumer assistance chatbot to direct the customer requests to the right channel of communication.

## Technologies

This project was developed using the following tools:

- Python
- Django
- Celery
- Redis

## Getting started

- Create virtual enviroment and activate it
- Run `pip install -r requirements.txt` to install dependencies
- Run `python manage.py migrate`to make migrations
- To start server, run `python manage.py runserver``
- To start Redis run `redis-server``
- Run `celery -A chatbot_backend.celery worker -l info`to run Celery worker
- Set up Ngrok anc connect tunnel
- Add Ngrok url to the chatbot webhook