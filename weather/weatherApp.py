
import pyowm
from config.config_reader import ConfigReader

class WeatherInformation():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.owmapikey = "d196a1e502460be6c85ebc506675a809"
        self.owm = pyowm.OWM(self.owmapikey)

    def get_weather_info(self,city):
        self.city=city
        print(self.city)
        observation = self.owm.weather_manager().weather_at_place(city)
        w = observation.weather
        latlon_res = observation.location
        print(w.status)
        '''
        lat = str(latlon_res.get_lat())
        lon = str(latlon_res.get_lon())
        

        wind_res = w.get_wind()
        wind_speed = str(wind_res.get('speed'))

        humidity = str(w.get_humidity())

        celsius_result = w.get_temperature('celsius')
        temp_min_celsius = str(celsius_result.get('temp_min'))
        temp_max_celsius = str(celsius_result.get('temp_max'))

        fahrenheit_result = w.get_temperature('fahrenheit')
        temp_min_fahrenheit = str(fahrenheit_result.get('temp_min'))
        temp_max_fahrenheit = str(fahrenheit_result.get('temp_max'))
        '''
        status=w.status
        detailed_status=w.detailed_status
        
        self.bot_says = "status: "+str(status)+"\n"+"     detailed_status: "+str(detailed_status)+"\n"
        return self.bot_says
