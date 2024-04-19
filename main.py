from weather_api import get_weather
from data_analysis import analyze_temperatures
from display import display_weather

def main():
    city = input("Podaj miasto: ")
    weather_data = get_weather(city)
    display_weather(weather_data)
    avg_temp = analyze_temperatures(weather_data)
    print(f"Średnia temperatura w najbliższe dni: {avg_temp}°C")

if __name__ == '__main__':
    main()
