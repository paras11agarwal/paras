from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Data(models.Model):
	user=models.ForeignKey(User,unique=True,on_delete=models.CASCADE)
	roll1=models.IntegerField()
	roll2=models.IntegerField()
	phone=models.IntegerField()

class Question(models.Model):
	question=models.ImageField(upload_to='img',null=False)
	answer=models.CharField(null=False,max_length=256)