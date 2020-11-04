from loader import dp
import aiohttp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram import types
from aiogram.types.message import ContentTypes

thunderstorm = u'\U0001F4A8'  # Code: 200's, 900, 901, 902, 905
drizzle = u'\U0001F4A7'  # Code: 300's
rain = u'\U00002614'  # Code: 500's
snowflake = u'\U00002744'  # Code: 600's snowflake
snowman = u'\U000026C4'  # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'  # Code: 700's foogy
clearSky = u'\U00002600'  # Code: 800 clear sky
fewclouds = u'\U000026C5'  # Code: 801 sun behind clouds
clouds = u'\U00002601'  # Code: 802-803-804 clouds general
hot = u'\U0001F525'  # Code: 904
defaultemoji = u'\U0001F300'  # default emojis
degree_sign = u'\N{DEGREE SIGN}'

def getEmoji(weatherID):
    if weatherID:
        if str(weatherID)[0] == '2' or weatherID == 900 or weatherID == 901 or weatherID == 902 or weatherID == 905:
            return thunderstorm
        elif str(weatherID)[0] == '3':
            return drizzle
        elif str(weatherID)[0] == '5':
            return rain
        elif str(weatherID)[0] == '6' or weatherID == 903 or weatherID == 906:
            return snowflake + ' ' + snowman
        elif str(weatherID)[0] == '7':
            return atmosphere
        elif weatherID == 800:
            return clearSky
        elif weatherID == 801:
            return fewclouds
        elif weatherID == 802 or weatherID == 803 or weatherID == 803:
            return clouds
        elif weatherID == 904:
            return hot
        else:
            return defaultemoji    # Default emoji

    else:
        return defaultemoji   # Default emoji

async def get_weather(city):
        async with aiohttp.ClientSession() as session:
            api_key = '2bb76f8309069d9d4dec6e0d4db99684'
            url = 'http://api.openweathermap.org/data/2.5/weather?&lang=ru&units=metric&q=' + city + '&appid=' + api_key
            async with session.get(url) as resp:
                data = await resp.json()
                countryName = data['sys']['country']
                cityName = data['name']
                if cityName == 'Moscow' and countryName != 'RU':
                    url1 = 'http://api.openweathermap.org/data/2.5/weather?&lang=ru&units=metric&id=524901&appid=2bb76f8309069d9d4dec6e0d4db99684'
                    async with session.get(url1) as resp:
                        data = await resp.json()
                else:
                    pass
                resultCode = str(data['cod'])
                if resultCode == '200':  # Success city found
                    cityName = data['name']
                    countryName = data['sys']['country']
                    temp_current = str(data["main"]["temp"])
                    temp_max = str(data["main"]["temp_max"])
                    temp_min = str(data["main"]["temp_min"])
                    description = data['weather'][0]['description']
                    description_brief = data['weather'][0]['main']
                    pressure = str(data["main"]["pressure"])
                    humidity = str(data["main"]["humidity"])
                    visibility = str(data["visibility"])
                    windspeed = str(data["wind"]["speed"])
                    weatherID = str(data['weather'][0]['id'])  # gets ID of weather description, used for emoji
                    emoji = getEmoji(weatherID)
                    weather_message = (f'{cityName}, {countryName}: *{str(temp_current)}*{degree_sign}C\n'
                                       f'Max: {temp_max}{degree_sign}C - Min: {temp_min}{degree_sign}C\n'
                                       f'{description_brief} - {description}{emoji}{emoji}\n'
                                       f'Pressure - {pressure} мм рт. ст.\n'
                                       f'Humidity - {humidity}%\n'
                                       f'Visibility - {visibility} meters\n'
                                       f'Wind speed - {windspeed} m.s.')
                    return weather_message

@dp.message_handler(Command("weather"))
async def weather(message: Message):
    if message.text == '/weather':
        await message.answer('Dear *' + message.from_user.first_name + '*! Select your city, for example /weather Moscow',
                         parse_mode='Markdown')
    else:
        try:
            text = message.text
            texts = text.split(' ', 1)
            city = str.upper(texts[1])
            await message.answer(await get_weather(city), parse_mode='Markdown')
        except Exception as e:
            await message.answer('Bro *' + message.from_user.first_name + '*, sorry, there is no such city, try again!',
                                 parse_mode='Markdown')

