from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	followers = models.ManyToManyField(User)

	def __str__(self):
		return self.title
