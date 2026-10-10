import requests

url = "https://aviationweather.gov"
response=requests.get(url)
data = response.json()
airpot_report = data[0]
wind_direction = airport_report.get('wdir')
wind_speed = airport_report.get('wspd')
print(wind_direction)
print(wind_speed)