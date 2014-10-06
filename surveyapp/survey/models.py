from django.db import models

# Create your models here.

class Choice(models.Model):
	text    = models.CharField(max_length=200)
	program = models.CharField(max_length=200)
        date    = models.DateField(auto_now_add=True)
