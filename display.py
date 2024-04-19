def display_weather(data):
    city = data['location']['name']
    current_temp = data['current']['temp_c']
    print(f"Pogoda dla {city}:")
    print(f"Aktualna temperatura: {current_temp}°C")
    print("Prognoza na najbliższe dni:")
    for day in data['forecast']['forecastday']:
        date = day['date']
        temp = day['day']['avgtemp_c']
        print(f"{date}: średnia temperatura {temp}°C")
