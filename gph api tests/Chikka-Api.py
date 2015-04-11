import requests as rq

clientId = "0b9bdff52c5fbef602a9b2b4cc1f88335e5f08f0fdd745a1e265ca52f14b66e0"
secretKy = "83b97c2a2423ce38f4b8f94b4f9587702f7cb50b785b2f2670be69fd1a0c86fd"
shortcode = 292904523


def sendMessage(msg,number,msgType):
	#msgType = "SEND" - > for solo msgs , REPLY for replying to a msg
	payload = { 'message_type' : msgType , 
				'mobile_number':number, 
				'shortcode':shortcode,
				'message_id':'ccc81279fcc048d1a6fcc52ed4c13255',
				'message' :msg,'client_id' : clientId,
				'secret_key':secretKy}
	r = rq.post('https://post.chikka.com/smsapi/request',data = payload)
	print(r.url)
	print(r.status_code)
	print(r.text)


#both requires urls
def rcvMessage():
	msgType = 'incoming'


def chkDeliveryOf(msg_id,status):
	
	#todo: timestamping
	msgType = "outgoing"
	payload = 
			{ 
				'message_type' : msgType , 
				'shortcode':shortcode,
				'message_id':'ccc81279fcc048d1a6fcc52ed4c13255',
				'client_id' : clientId,
				'secret_key':secretKy
			}