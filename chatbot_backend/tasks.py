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
    sleep(60)
    send_mail(
        'Hello from Umishop',
        'Hello welcome to Umishop',
        'from@umishop.com',
        [email],
        fail_silently=False,
    )
@shared_task()
def send_assistance_email_task(text):
    send_mail(
        'Sales assistance request',
        text,
        'assistancebot@umishop.com',
        ['sales@umishop.com'],
        fail_silently=False,
    )