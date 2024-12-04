import requests


def get_coordinates(city, country, key_api):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": f"{city},{country}", "limit": 1, "appid": key_api}
    response = requests.get(url, params=params, verify= False)

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            print(f"{country}, {city} coordinates: lat {lat}, lon {lon}")
            return lat, lon
        else:
            print(f"{country}, {city}  no result .")
            return None, None
    else:
        print(f"Hata: {response.status_code} - {response.text}")
        return None, None


# koordinatlarını aldığımız bölgenin hava durumunu getirelim.
# OpenWeatherMap API'sinden hava durumu bilgilerini almaya yarayan fonksiyon
def get_weather(lat, lon, key_api):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": key_api,
        "units": "metric"  # sıcaklık birimi (celsius)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather Condition: {data['weather'][0]['description']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

api_key = "f5fcdfb3e9a5ecc95aa288cb951df67f"

Country = input("Country: ")
City = input("City: ")
# Koordinatları al ve hava durumu tahminlerini getir
Lat, Lon = get_coordinates(City, Country, api_key)
# Koordinatlar doğru şekilde alınmış mı kontrol et
if Lat is None or Lon is None:
    print("Hata: Koordinatlar alınamadı.")
else:
    print(Lat)
    print(Lon)
    get_weather(Lat, Lon, api_key)



