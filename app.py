import requests

API_KEY = "11c8ea020a0640211c3b2206bb683172"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # For Celsius
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature} °C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")
else:
    print("City not found. Try again.")