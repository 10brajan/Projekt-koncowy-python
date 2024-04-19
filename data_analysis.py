def analyze_temperatures(data):
    forecast_days = data['forecast']['forecastday']
    temperatures = [day['day']['avgtemp_c'] for day in forecast_days]
    return sum(temperatures) / len(temperatures)
