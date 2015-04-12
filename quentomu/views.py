from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from apis.gph_api_tests import Chikka_Api as chk,hasher as hs
import requests as rq
from django.core.mail import send_mail
import types

global content
content = ''
def home(request):
	if request.user.is_anonymous():
		return render(request, 'index.html')
	else:
		topics = Topic.objects.all()
		messages = Message.objects.all()

		return render(request, 'home.html',
			{"topics": topics, "messages": messages.__dict__}
		)

def Remittance(request):
	pass
def DeliveryNotif(request,number):
	hashed =hs.hashme(number)
	r = chk.sendMessage(str(hashed),number,'SEND', hashed )
	global content 
	content = "I sent a message "+ r.text + " "+ str(r.status_code)
	send_mail('Sent message by '+str(hashed), content, 'pagong@quentomu.herokuapp.com',
    ['pjinxed.aranzaellej@gmail	.com'], fail_silently=False)
	r = chk.chkDeliveryOf()
	content = "I confirmed the sent message by "+ str(hashed),+ r.text + " "+ str(r.status_code)
	send_mail('Confirm msg sent by' +str(hashed), content, 'pagong@quentomu.herokuapp.com',
    ['pjinxed.aranzaellej@gmail	.com'], fail_silently=False)
    return render(request, 'home.html',
			{"topics": topics, "messages": messages.__dict__}
		)
def ReceivedMsgs(request):
	r = chk.rcvMessage()
	global content
	content = "Message Recieved "+r.text+" "+ str(r.status_code)

def conversation(request):
	if request.method == 'POST':

		print(request.body)

		print (User.objects.get(id=request.body['friend_id']))

		Message(
			sender=request.user,
			receiver=User.objects.get(id=request.body['friend_id'])[0],
			content=request.body['reply']
		).save()

		return JsonResponse({"successful": True})
	else:
		messages = Message.objects.filter(
			Q(sender=request.user) |
			Q(receiver=request.user)
		)

		people_conversed_with = set([
			message.contact_number
				if message.contact_number is not ''
			else message.sender
				if message.sender is not ''
					and message.sender != request.user
			else message.receiver
		for message in messages])

		conversations = [
			{
				'friend': friend if type(friend) is str
					else {"id": friend.id, "username": friend.username},
				'messages': [
					{
						"you": message.sender == request.user,
						"content": message.content
					}
					for message in messages
					if message.sender == friend or message.receiver == friend
					or message.contact_number == friend
				]
			}
			for friend in people_conversed_with
		]

		return JsonResponse(conversations, safe=False);

def topics(request):
	messages = Message.objects.filter(
		Q(sender=request.user) |
		Q(receiver=request.user)
	)
	messages = [{
		'sender': message.sender.username if message.sender else None ,
		'receiver': message.receiver.username if message.receiver else None,
		'content': message.content,
		'contact_number': message.contact_number,
	} for message in messages]

	print(messages)

	return JsonResponse(messages, safe=False);
