import requests as rq

clientId = "0b9bdff52c5fbef602a9b2b4cc1f88335e5f08f0fdd745a1e265ca52f14b66e0"
secretKy = "83b97c2a2423ce38f4b8f94b4f9587702f7cb50b785b2f2670be69fd1a0c86fd"
shortcode = 292904523
rqID =  ''
rqCost = ''


def sendMessage(msg,number,msgType,msgID):
	#msgType = "SEND" - > for solo msgs , REPLY for replying to a msg
	payload = { 'message_type' : msgType , 
				'mobile_number':number, 
				'shortcode':shortcode,
				'message_id':msgID,
				'message' :msg,'client_id' : clientId,
				'secret_key':secretKy,
				('request_id' if msgType=='REPLY' else ''):( rqID if msgType=='REPLY' else ''),
				('request_cost' if msgType=='REPLY' else ''):( rqCost if msgType=='REPLY' else '')

				}
	r = rq.post('https://post.chikka.com/smsapi/request',data = payload)
	print(r.url)
	print(r.status_code)
	print(r.text)


#both requires urls
def rcvMessage():
	msgType = 'incoming'
	msgID = ''
	timestamp = ''
	payload = 
			{
				'message_type' : msgType , 
				'shortcode':shortcode,
				'message_id':msgID,
				'client_id' : clientId,
				'request_id' : rqID
				'timestamp': timestamp
			}
	r  = rq.get('https://post.chikka.com/smsapi/request',data = payload)
	print (r.text)
	print(r.url)
	if(r):
		payload = {'Status' : 'Accepted'}
		print("accepted")
		r = rq.post('https://post.chikka.com/smsapi/request')
	else
		payload = {'Status' : 'Error'}
		print("Error")
		r = rq.post('https://post.chikka.com/smsapi/request')



def chkDeliveryOf():
	
	#todo: timestamping
	msgType = "outgoing"
	payload = 
			{ 
				'message_type' : msgType , 
				'shortcode':shortcode,
				'message_id':msgID,
				'client_id' : clientId,
				'secret_key':secretKy
			}
	r = rq.get('https://post.chikka.com/smsapi/request',data = payload)
	print(r.text)
	print(r.url)
	if(r):
		payload = {'Status' : 'Accepted'}
		print("accepted")
		r = rq.post('https://post.chikka.com/smsapi/request')
	else
		payload = {'Status' : 'Error'}
		print("Error")
		r = rq.post('https://post.chikka.com/smsapi/request')
