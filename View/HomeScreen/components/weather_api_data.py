import requests

def get_weather(city):

	url = "https://yahoo-weather5.p.rapidapi.com/weather"

	querystring = {"location":city,"format":"json","u":"f"}

	headers = {
		"x-rapidapi-key":"your-api-key",
		"x-rapidapi-host":"yahoo-weather5.p.rapidapi.com"
		}

	try:
		response =requests.get(url, headers=headers,params=querystring)
		return response.json()
	except Exception as e:
		return False
