import requests

def get_weather(city):

	api_key="your-api-key"
	url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

	try:
		response =requests.get(url)
		return response.json()
	except Exception as e:
		return False
