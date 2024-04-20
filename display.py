from weather_api import get_weather
from data_analysis import analyze_temperatures

def display_weather(data):
    try:
        city = data['location']['name']
        current_temp = data['current']['temp_c']
        print(f"Pogoda dla {city}:")
        print(f"Aktualna temperatura: {current_temp}°C")
        print("Prognoza na najbliższe dni:")
        for day in data['forecast']['forecastday']:
            date = day['date']
            temp = day['day']['avgtemp_c']
            print(f"{date}: średnia temperatura {temp}°C")
    except KeyError as e:
        print(f"Błąd: Brak klucza {e} w odpowiedzi API.")

def run_application():
    while True:
        city = input("Podaj miasto (wpisz 'quit' aby zakończyć): ")
        if city.lower() == 'quit':
            print("Zakończenie programu.")
            break
        try:
            weather_data = get_weather(city)
            display_weather(weather_data)
            avg_temp = analyze_temperatures(weather_data)
            print(f"Średnia temperatura w najbliższe dni: {avg_temp}°C")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
