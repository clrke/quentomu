import requests as rq
from urllib.parse import urlencode

app_id = "02FLzuJ5jxn5wP0aqzhD"
app_code = "AkwssyI7EukQ3epwH8Z5-Q"

def geocode_search(search):
	try:
		payload = {
			'searchtext': search,
			'app_id' : app_id,
			'app_code' : app_code,
			'gen': '6'
		}
		r = rq.get("https://geocoder.cit.api.here.com/6.2/geocode.json?%s"%
			urlencode(payload))

		geocode = r.json()

		# return geocode['Response']['View'][0]['']
		nav_pos = geocode['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]

		latitude = nav_pos['Latitude']
		longitude = nav_pos['Longitude']

		return "%s,%s"%(latitude, longitude)
	except:
		return None

def geo_pedroute(origin, dest):
	payload = {
		'waypoint0': origin,
		'waypoint1' : dest,
		'app_code' : app_code,
		'app_id' : app_id,
		'mode': 'fastest;pedestrian'
	}
	r = rq.get("https://route.cit.api.here.com/routing/7.2/calculateroute.json",params=payload)
	return r.text

def geo_carroute(origin, dest):
	try:
		payload = {
			'waypoint0': origin,
			'waypoint1' : dest,
			'app_code' : app_code,
			'app_id' : app_id,
			'mode': 'fastest;car;traffic:enabled',
			'departure': 'now'
		}

		r = rq.get("https://route.cit.api.here.com/routing/7.2/calculateroute.json?%s"%
			urlencode(payload))

		route = r.json()

		distance = route['response']['route'][0]['summary']['distance']

		return distance
	except:
		return 0

def geo_transroute(origin, dest):
	payload = {
		'waypoint0': origin,
		'waypoint1' : dest,
		'app_code' : app_code,
		'app_id' : app_id,
		'mode': 'fastest;publicTransport',
		'combineChange': 'true'
	}
	r = rq.get("https://route.cit.api.here.com/routing/7.2/calculateroute.json",data =payload)
	return r.text
