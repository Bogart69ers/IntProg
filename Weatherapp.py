import requests

api_key = '1d228b8fc14ec06da1ca310c4d8e7d13'

user_input = input("Enter City: ")

weather_urlreq = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")

if weather_urlreq.status_code == 404:
    print("No City Found")
elif weather_urlreq.status_code == 200:
    weather_data = weather_urlreq.json()
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    humidity = (weather_data)['main']['humidity']
    
    Cel = ((temp-32)*0.56)

    print(f"The weather in {user_input} is: {weather}")
    print(f"The Temperature in {user_input} is: {Cel :.2f}°C / {temp}°F")
    print(f"The Humidity in {user_input} is: {humidity}%")
else:
    print(f"Error: Unable to retrieve weather data. Status code: {weather_urlreq.status_code}")
