
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .tasks import send_email_task

class ChatUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=257, unique = True, blank = False)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)

    def send_email(self):
        send_email_task.delay(self['email'])

    def __str__(self):
        return self.name + ' ' + self.email
class AssistanceRequest(models.Model):
    topic = models.CharField(max_length=200)
    text = models.CharField(max_length = 500)

    def send_email(self):
        send_email_task.delay(self['email'])

    def __str__(self):
        return self.topic + ' ' + self.text