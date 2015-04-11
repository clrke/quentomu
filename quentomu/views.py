from django.shortcuts import render
from .models import *

def home(request):
	topics = Topic.objects.all()
	messages = Message.objects.all()

	return render(request, 'home.html',
		{"topics": topics, "messages": messages}
	)
