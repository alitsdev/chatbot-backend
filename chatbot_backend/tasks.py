#from .celery import app
from time import sleep
from django.core.mail import send_mail
from celery import shared_task

#@app.task(bind=True)
#def debug_task(self):
    #print('Request: {0!r}'.format(self.request))
#@app.task(bind=True)
@shared_task()
def send_email_task(email):
    print('hola')
    print(email)
    sleep(60)
    send_mail(
        'Hello from Umishop',
        'Hello welcome to Umishop',
        'from@example.com',
        [email],
        fail_silently=False,
    )