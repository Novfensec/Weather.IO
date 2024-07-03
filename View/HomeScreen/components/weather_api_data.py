import requests

def get_weather(city):
	
	url = "https://yahoo-weather5.p.rapidapi.com/weather"

	querystring = {"location":city,"format":"json","u":"f"}

	headers = {
		"x-rapidapi-key": "0fafe3de48mshce9c7b8d2fa9c1ap194196jsn2e9237f5a2c8",
		"x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
		}
    
	try:
		response =requests.get(url, headers=headers,params=querystring)
		return response.json()
	except Exception as e:
		return True
