import requests as rq

clientId = "0b9bdff52c5fbef602a9b2b4cc1f88335e5f08f0fdd745a1e265ca52f14b66e0"
secretKy = "83b97c2a2423ce38f4b8f94b4f9587702f7cb50b785b2f2670be69fd1a0c86fd"
shortcode = 292904523

rqCost = 'FREE'


def sendMessage(msg,number,msgType,msgID,rqID):
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
	return r


#both requires urls
def rcvMessage():
	msgType = 'incoming'
	msgID = ''
	timestamp = ''
	msg =''
	mobile_number = ''
	payload = {	
				'message_type' : msgType ,
				'mobile_number' : mobile_number,
				'message' : msg,
				'secret_key' : secretKy,
				 'shortcode' : shortcode ,
				'message_id':msgID,
				'client_id' : clientId,
				'request_id' : rqID,
				'timestamp': timestamp
		}
	r  = rq.get('https://post.chikka.com/smsapi/request',data = payload)
	print (r.text)
	print(r.url)
	if(r):
		payload = {'Status' : 'Accepted'}
		print("accepted")
		r = rq.post('https://post.chikka.com/smsapi/request')
	else:
		payload = {'Status' : 'Error'}
		print("Error")
		r = rq.post('https://post.chikka.com/smsapi/request')
	return r



def chkDeliveryOf():
	
	#todo: timestamping
	msgType = "outgoing"
	msgID = ''
	number = ''
	status = ''
	timestamp = '' 
	credits_cost = ''
	payload = { 
				'message_type' : msgType , 
				'shortcode':shortcode,
				'message_id':msgID,
				'status': status,
				'timestamp' : timestamp,
				'credits_cost': credits_cost,
			}
	r = rq.post('https://post.chikka.com/smsapi/request',data = payload)
	print(r.text)
	print(r.url)
	if(r):
		payload = {'Status' : 'Accepted'}
		
		r = rq.post('https://post.chikka.com/smsapi/request' , data = payload)
	else:
		payload = {'Status' : 'Error'}
		
		r = rq.post('https://post.chikka.com/smsapi/request' , data = payload)
	return r