import aiohttp
from config import api_key

async def get_weather(city: str) -> str:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
        if data["cod"] != 200:
            return 'City not found ❌'

        name = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]

        return f"📍 {name}\n\n🌡️ Temp: {temp}°C\n🤔 Feels like: {feels_like}°C\n☁️ {desc.capitalize()}"
    except Exception as e:
        print("❌ Error in get_weather:", e)
        return "⚠️ Error retrieving the weather."