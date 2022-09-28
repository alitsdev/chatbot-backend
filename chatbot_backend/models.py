from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ChatUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=257, unique = True, blank = False)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)

    def __str__(self):
        return self.name + ' ' + self.email