from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	followers = models.ManyToManyField(User)

	def __str__(self):
		return self.title

class Message(models.Model):
	sender = models.ForeignKey(User, related_name='sender_id')
	receiver = models.ForeignKey(User, related_name='receiver_id')
	content = models.CharField(max_length=160)
	contact_number = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return "[%s to %s] %s"%(self.sender.id, self.receiver.id, self.content)
