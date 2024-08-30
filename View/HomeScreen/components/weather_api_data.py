import requests

def get_weather(city):

	url = "https://yahoo-weather5.p.rapidapi.com/weather"

	querystring = {"location":city,"format":"json","u":"f"}

	headers = {
		"x-rapidapi-key":"1ac7e92d6bmshd62b76e95f16cd4p15ed25jsnc2f2fa37441d",
		"x-rapidapi-host":"yahoo-weather5.p.rapidapi.com"
		}

	try:
		response =requests.get(url, headers=headers,params=querystring)
		return response.json()
	except Exception as e:
		return False
