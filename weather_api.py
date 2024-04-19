import requests

def get_weather(city):
    api_key = "592b61084cb548dba69104555241504"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"
    response = requests.get(url)
    return response.json()
