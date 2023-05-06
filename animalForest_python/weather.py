import requests
import json

city = "Seoul"
API = "aeaf7b3962075832933ae63beaaa2ba0"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)
print(data)
print("----------------")


print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["description"], "입니다.")
print("현재 온도는 ", data["main"]['temp'],"입니다.")
print("하지만 체감", data["main"]['feels_like'], "일 거에요.")
print("최저 기온은", data["main"]['temp_min'], "입니다.")
print("최고 기온은", data["main"]['temp_max'], "입니다.")
print("습도는", data["main"]['humidity'], "입니다.")
print("기압은", data["main"]['pressure'], "입니다.")
print("풍향은", data["wind"]['deg'], "입니다.")
print("풍속은", data["wind"]['speed'], "입니다.")

# {'coord': {'lon': 126.9778, 'lat': 37.5683},
#     'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}],
#     'base': 'stations',
#     'main': {'temp': 285.9, 'feels_like': 285.45, 'temp_min': 284.84, 'temp_max': 285.93, 'pressure': 1007, 'humidity': 85},
#     'visibility': 10000,
#     'wind': {'speed': 4.63, 'deg': 30},
#     'rain': {'1h': 0.56}, 'clouds': {'all': 100}, 'dt': 1683348366, 'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1683318724, 'sunset': 1683368723}, 'timezone': 32400, 'id': 1835848, 'name': 'Seoul', 'cod': 200}