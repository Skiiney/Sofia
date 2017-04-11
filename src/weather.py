import pyowm

class Weather:
    def GetTemperature(city, token):
        owm = pyowm.OWM(token)
        observation = owm.weather_at_place(city+',br')
        weather_info = observation.get_weather()
        weather_split = str(weather_info).split('=')
        weather_status = str(weather_split[2]).replace('>','')

        if weather_status == 'Clouds':
            weather_status = weather_status+' :cloud:'
        elif weather_status == 'Clear':
            weather_status = weather_status+' :white_sun_small_cloud:'
        elif weather_status == 'Rain' or weather_status == 'Drizzle':
            weather_status = weather_status+' :cloud_rain:'
        elif weather_status == 'Thunderstorm':
            weather_status = weather_status+' :thunder_cloud_rain:'

        temperature = str(weather_info.get_temperature('celsius')).split(',')
        temperature_status = str(temperature[0]).replace('{\'temp\': ','')

        wind_info = str(weather_info.get_wind()).split(',')
        wind_status = str(wind_info[0]).replace('{\'speed\': ','')

        humidity = str(weather_info.get_humidity())

        return weather_status, temperature_status, wind_status, humidity
