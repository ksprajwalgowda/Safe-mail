from django.db import models

# Create your models here.

class Mailbox(models.Model):
    to = models.CharField(max_length=50, verbose_name = "to")
    sender = models.CharField(max_length=50, verbose_name = "sender")
    sub = models.CharField( max_length=50, verbose_name = "subject" ,null=True)
    message = models.TextField(verbose_name="message")
