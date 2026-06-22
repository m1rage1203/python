import requests

from main import API


def get_weather(city):
    resp = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": API, "units": "metric", "lang": "ru"},
        timeout=5,
    )

    if resp.status_code == 401:
        return {"error": "Неверный API ключ"}
    if resp.status_code == 404:
        return {"error": f"Город '{city}' не найден"}

    data = resp.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
    }


if __name__ == "__main__":
    city = input("Введите город: ")
    result = get_weather(city)

    if "error" in result:
        print(f"Ошибка: {result['error']}")
    else:
        print(f"Город: {result['city']}")
        print(f"Температура: {result['temperature']}°C")
        print(f"Погода: {result['description']}")
        print(f"Влажность: {result['humidity']}%")
        print(f"Ветер: {result['wind']} м/с")
