import requests as rq

app_id = "02FLzuJ5jxn5wP0aqzhD"
app_code = "AkwssyI7EukQ3epwH8Z5-Q" 

def geocode_search(search):
	payload = {
		'searchtext': search,
		'app_id' : app_id,
		'app_code' : app_code,
		'gen': '6'
	}
	r = rq.get("https://geocoder.cit.api.here.com/6.2/geocode.json?",data =payload)
	return r.text

def geo_pedroute(origin, dest):
	payload = {
		'waypoint0': origin,
		'waypoint1' : dest,
		'app_code' : app_code,
		'app_id' : app_id,
		'mode': 'fastest;pedestrian'
	}
	r = rq.get("https://geocoder.cit.api.here.com/6.2/calculateroute.json?",data =payload)
	return r.text


def geo_carroute(origin, dest):
	payload = {
		'waypoint0': origin,
		'waypoint1' : dest,
		'app_code' : app_code,
		'app_id' : app_id,
		'mode': 'fastest;car;traffic:enabled',
		'departure': 'now'
	}
	r = rq.get("https://geocoder.cit.api.here.com/6.2/calculateroute.json?",data =payload)
	return r.text


def geo_transroute(origin, dest):
	payload = {
		'waypoint0': origin,
		'waypoint1' : dest,
		'app_code' : app_code,
		'app_id' : app_id,
		'mode': 'fastest;publicTransport',
		'combineChange': 'true'
	}
	r = rq.get("https://geocoder.cit.api.here.com/6.2/calculateroute.json?",data =payload)
	return r.text
