import requests
import datetime
import sqlite3

DB = "app.db"

class Weather():

    def __init__(self):
        self.creatat = None
        self.changeat = None
        self.w_lon = None
        self.w_lat = None
        self.s_weather_id = None
        self.s_weather_main = None
        self.s_weather_description = None
        self.s_weather_icon = None
        self.w_base = None
        self.s_main_temp = None
        self.s_main_feels_like = None
        self.s_main_temp_min = None
        self.s_main_temp_max = None
        self.s_main_pressure = None
        self.s_main_humidity = None
        self.s_main_sea_level = None
        self.s_main_grnd_level = None
        self.s_visibility = None
        self.s_wind_speed = None
        self.s_wind_deg = None
        self.s_wind_gust = None
        self.s_clouds = None
        self.w_rain_1h = None
        self.s_rain_3h = None
        self.w_snow_1h = None
        self.s_snow_3h = None
        self.s_dt = None
        self.w_sys_type = None
        self.w_sys_id = None
        self.w_sys_country = None
        self.w_sys_sunrise = None
        self.w_sys_sunset = None
        self.w_timezone = None
        self.w_id = None
        self.w_name = None
        self.s_cod = None
        self.f_message = None
        self.f_cnt = None
        self.f_temp_kf = None
        self.f_pop = None
        self.f_sys_pod = None
        self.f_dt_txt = None

    def fill(self, weather):
        self.creatat = datetime.datetime.now()
        #print(self.creatat)
        self.changeat = datetime.datetime.now()
        #print(self.changeat)
        self.w_lon = weather.get('coord').get('lon')
        #print(self.w_lon)
        self.w_lat = weather.get('coord').get('lat')
        #print(self.w_lat)
        self.s_weather_id = weather.get('weather')[0].get('id')
        #print(self.s_weather_id)
        self.s_weather_main = weather.get('weather')[0].get('main')
        #print(self.s_weather_main)
        self.s_weather_description = weather.get('weather')[0].get('description')
        #print(self.s_weather_description)
        self.s_weather_icon = weather.get('weather')[0].get('icon')
        #print(self.s_weather_icon)
        self.w_base = weather.get('base')
        #print(self.w_base)
        self.s_main_temp = weather.get('main').get('temp')
        #print(self.s_main_temp)
        self.s_main_feels_like = weather.get('main').get('feels_like')
        #print(self.s_main_feels_like)
        self.s_main_temp_min = weather.get('main').get('temp_min')
        #print(self.s_main_temp_min)
        self.s_main_temp_max = weather.get('main').get('temp_max')
        #print(self.s_main_temp_max)
        self.s_main_pressure = weather.get('main').get('pressure')
        #print(self.s_main_pressure)
        self.s_main_humidity = weather.get('main').get('humidity')
        #print(self.s_main_humidity)
        self.s_main_sea_level = weather.get('main').get('sea_level')
        #print(self.s_main_sea_level)
        self.s_main_grnd_level = weather.get('main').get('grnd_level')
        #print(self.s_main_grnd_level)
        self.s_visibility = weather.get('visibility')
        #print(self.s_visibility)
        self.s_wind_speed = weather.get('wind').get('speed')
        #print(self.s_wind_speed)
        self.s_wind_deg = weather.get('wind').get('deg')
        #print(self.s_wind_deg)
        self.s_wind_gust = weather.get('wind').get('gust')
        #print(self.s_wind_gust)
        self.s_clouds = weather.get('clouds').get('all')
        #print(self.s_clouds)
        if (weather.get('rain')):
            self.w_rain_1h = weather.get('rain').get('1h')
            self.s_rain_3h = weather.get('rain').get('3h')
        #print(self.w_rain_1h)
        #print(self.s_rain_3h)
        if (weather.get('snow')):
            self.w_snow_1h = weather.get('snow').get('1h')
            self.s_snow_3h = weather.get('snow').get('3h')
        #print(self.w_snow_1h)
        #print(self.s_snow_3h)
        self.s_dt = weather.get('dt')
        #print(self.s_dt)
        self.w_sys_type = weather.get('sys').get('type')
        #print(self.w_sys_type)
        self.w_sys_id = weather.get('sys').get('id')
        #print(self.w_sys_id)
        self.w_sys_country = weather.get('sys').get('country')
        #print(self.w_sys_country)
        self.w_sys_sunrise = weather.get('sys').get('sunrise')
        #print(self.w_sys_sunrise)
        self.w_sys_sunset = weather.get('sys').get('sunset')
        #print(self.w_sys_sunset)
        self.w_timezone = weather.get('timezone')
        #print(self.w_timezone)
        self.w_id = weather.get('id')
        #print(self.w_id)
        self.w_name = weather.get('name')
        #print(self.w_name)
        self.s_cod = weather.get('cod')
        #print(self.s_cod)
        self.f_message = weather.get('message')
        #print(self.f_message)
        self.f_cnt = weather.get('cnt')
        #print(self.f_cnt)
        self.f_temp_kf = weather.get('main').get('temp_kf')
        #print(self.f_temp_kf)
        self.f_pop = weather.get('pop')
        #print(self.f_pop)
        self.f_sys_pod = weather.get('sys').get('pod')
        #print(self.f_sys_pod)
        self.f_dt_txt = weather.get('dt_txt')
        #print(self.f_dt_txt)

    def write(self, con):
        con.execute('''insert into weather (creatat, changeat, w_lon, w_lat, s_weather_id, s_weather_main,
        s_weather_description, s_weather_icon, w_base, s_main_temp, s_main_feels_like, s_main_temp_min, s_main_temp_max,
        s_main_pressure, s_main_humidity, s_main_sea_level, s_main_grnd_level, s_visibility, s_wind_speed,
        s_wind_deg, s_wind_gust, s_clouds, w_rain_1h, s_rain_3h, w_snow_1h, s_snow_3h, s_dt, w_sys_type,
        w_sys_id, w_sys_country, w_sys_sunrise, w_sys_sunset, w_timezone, w_id, w_name, s_cod, f_message,
        f_cnt, f_temp_kf, f_pop, f_sys_pod, f_dt_txt) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
        [self.creatat, self.changeat, self.w_lon, self.w_lat, self.s_weather_id, self.s_weather_main,
        self.s_weather_description, self.s_weather_icon, self.w_base, self.s_main_temp, self.s_main_feels_like,
        self.s_main_temp_min, self.s_main_temp_max, self.s_main_pressure, self.s_main_humidity, self.s_main_sea_level,
        self.s_main_grnd_level, self.s_visibility, self.s_wind_speed, self.s_wind_deg, self.s_wind_gust, self.s_clouds,
        self.w_rain_1h, self.s_rain_3h, self.w_snow_1h, self.s_snow_3h, self.s_dt, self.w_sys_type, self.w_sys_id, self.w_sys_country,
        self.w_sys_sunrise, self.w_sys_sunset, self.w_timezone, self.w_id, self.w_name, self.s_cod, self.f_message, self.f_cnt,
        self.f_temp_kf, self.f_pop, self.f_sys_pod, self.f_dt_txt])


weathers = []

with open("apikey.txt") as file:
    apikey = file.read()

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Praha&APPID={apikey}&units=metric')

#print(response.status_code)

weather = Weather()
#print(weather.changeat)

if (response.status_code == 200):
    weather.fill(response.json())
    weathers.append(weather)

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q=Praha&APPID={apikey}&units=metric')

#print(response.status_code)

if (response.status_code == 200):
    data = response.json()
    data1 = dict((i, data[i]) for i in data if i!='list' and i!='city')
    data2 = data1 | data.get('city')
    for i in range(len(data.get('list'))):
        data3 = data2 | data.get('list')[i]
        weather = Weather()
        #print(weather.changeat)
        weather.fill(data3)
        weathers.append(weather)

con = sqlite3.connect(DB)
#con.row_factory = sqlite3.Row
con.execute(f"delete from weather;")
con.commit()
#con.execute(f"insert into weather (w_lon) values(?);", [1])
for weather in weathers:
    weather.write(con)
con.commit()
cur = con.execute(f"SELECT * FROM weather;")
data = cur.fetchall()
con.close()