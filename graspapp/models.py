from django.db import models

# Create your models here.
class subscribers(models.Model):
    email = models.EmailField(max_length=100,  null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.email

class Mailmessage(models.Model):
    title = models.CharField(max_length=100, null = True)
    message = models.TextField(null=True)

    def __str__(self):
       return self.title