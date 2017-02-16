from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Detail(models.Model):
	email=models.CharField(max_length=200)
	token=models.CharField(max_length=200)
	session=models.CharField(max_length=1)

	def __str__(self):
		return self.email

	def return_mail(self):
		return self.email
	
	def return_token(self):
		return self.token
	
	def return_session(self):
		return self.session

