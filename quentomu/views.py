from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import *
from apis.gph_api_tests import Chikka_Api as chk,hasher as hs
import requests as rq
from django.core.mail import send_mail
import types
import json
from apis.gph_api_tests import Here as here

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
def DeliveryNotif(request,number,msg):
	return HttpResponse(deliver())

def deliver(number, msg):
	hashed =hs.hashme(number)
	r = chk.sendMessage(msg,number,'SEND', hashed , '')
	global content
	content = "I sent a message "+ r.text + " "+ str(r.status_code)
	send_mail('Sent message by '+str(hashed), content, 'pagong@quentomu.herokuapp.com',
	['pjinxed.aranzaellej@gmail	.com'], fail_silently=False)

	return 'Successful'

def DeliveryNotif_reply(request, number,reqID,msg):
	r = chk.sendMessage(msg,number,'REPLY', hashed , reqID )
	global content
	content = "I sent a message "+ r.text + " "+ status_coder(r.status_code)
	send_mail('Sent message by '+str(hashed), content, 'pagong@quentomu.herokuapp.com',
	['pjinxed.aranzaellej@gmail	.com'], fail_silently=False)
	return HttpResponse('successful')

def DN(request):
	r = chk.chkDeliveryOf()
	content = "I confirmed the sent message by "+ str(hashed)+ r.text + " "+ str(r.status_code)
	send_mail('Confirm msg sent by' +str(hashed), content, 'pagong@quentomu.herokuapp.com',
	['pjinxed.aranzaellej@gmail.com'], fail_silently=False)

def ReceivedMsgs(request):
	r = chk.rcvMessage()
	global content
	content = "Message Recieved by "+ str(hashed)+ r.text + " "+ str(r.status_code)
	send_mail('inbox by' +str(hashed), content, 'pagong@quentomu.herokuapp.com',
	['pjinxed.aranzaellej@gmail.com'], fail_silently=False)

def conversation(request):
	if request.method == 'POST':
		POST = json.loads(request.body.decode("utf-8"))

		if type(POST['friend_id']) is str:
			receiver = User.objects.get(id=1)
			contact_number = POST['friend_id']
		else:
			receiver = User.objects.get(id=POST['friend_id'])
			contact_number=''

		Message(
			sender=request.user,
			receiver=receiver,
			content=POST['reply'],
			contact_number=contact_number
		).save()

		if contact_number != '':
			deliver(contact_number, POST['reply'])

		return JsonResponse({"successful": True})
	else:
		messages = Message.objects.filter(
			Q(sender=request.user) |
			Q(receiver=request.user)
		).order_by('id')

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
				],
				'distance': get_distance(friend.id, request.user.id)['distance']
					if type(friend) is not str else None
			}
			for friend in people_conversed_with
		]

		return JsonResponse(conversations, safe=False);

def topics(request):
	topics = [{
		"id": topic.id,
		"title": topic.title,
		"body": topic.body,
		"posts_count": topic.post_set.count()
	} for topic in Topic.objects.all()]

	return JsonResponse(topics, safe=False);

def topics_create(request, id):
	if request.method == 'POST':
		topic = Topic.objects.get(id=id)

		Post(
			title=request.POST['post'],
			author=request.user,
			parent=None,
			topic=topic
		).save()

		return redirect("/topics/%d"%topic.id)
	else:
		topic = Topic.objects.get(id=id)
		return render(request, 'topics/create.html', {"topic": topic})


def get_replies(post):
	replies = post.post_set.all()

	for reply in replies:
		reply.replies = get_replies(reply)

	return replies

def topics_show(request, id):
	topic = Topic.objects.get(id=id)
	original_posts = topic.post_set.filter(parent=None)

	for post in original_posts:
		post.replies = get_replies(post)

	return render(request, 'topics/show.html', {
		"topic": topic,
		"original_posts": original_posts,
	})

def get_original_post(post):
	if post.parent == None:
		return post
	else:
		return get_original_post(post.parent)

def topics_reply(request, id):
	if request.method == 'POST':
		post = Post.objects.get(id=id)

		Post(
			title=request.POST['reply'],
			author=request.user,
			parent=post,
			topic=post.topic
		).save()

		return redirect("/topics/%d"%post.topic.id)
	else:
		post = Post.objects.get(id=id)

		return render(request, 'topics/reply.html', {"post": post})

def distance(request, user1_id, user2_id):
	return JsonResponse(get_distance(user1_id, user2_id), safe=False)

def get_distance(user1_id, user2_id):
	user1 = User.objects.get(id=user1_id)
	user2 = User.objects.get(id=user2_id)

	address1 = user1.address.value
	address2 = user2.address.value

	geocode1 = here.geocode_search(address1)
	geocode2 = here.geocode_search(address2)

	distance = here.geo_carroute(geocode1, geocode2)

	return {
		"addresses": [address1, address2],
		"geocode": [geocode1, geocode2],
		"distance": round(distance/1000, 1),
	}
