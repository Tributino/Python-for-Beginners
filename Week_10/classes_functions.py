# coding: utf-8



def get_keys(dl):
    keys = []
    if isinstance(dl, list):
        keys += get_keys(dl[0])
    if isinstance(dl, dict):
        keys += dl.keys()
        for key in dl.keys():
            keys += get_keys(dl[key])
    return keys


class CountryInsert:
    
    sql = "INSERT OR IGNORE INTO Country (country_code) VALUES ( ? )"
    
    def __init__(self, country_code):
        self.country_code = country_code
    
    def countryInfo(self):
   
        return self.sql, (self.country_code,) 

    def __dir__(self):
        return ['country_code', 'countryInfo()']    

    def __str__(self):
        return 'countryTable'  

class CityInsert:
    
    sql = '''INSERT OR IGNORE INTO City (id, city_name, country_id, latitude, longitude) 
                VALUES ( ?, ?, ?, ?, ? )'''
    
    def __init__(self, dic_city):
        self.dic_city = dic_city 
        
    def cityInfo(self, country_id):

        city_id = self.dic_city['id']
        city_name = self.dic_city['name']
        lon = self.dic_city['coord']['lon']
        lat = self.dic_city['coord']['lat']

        return self.sql, (city_id, city_name, country_id, lat, lon) 
    
    def __dir__(self):
        return ['dic_city', 'cityInfo(country_id)']  

    def __str__(self):
        return 'cityTable'  

from datetime import datetime
class TempInsert:
    
    sql = '''INSERT OR REPLACE INTO Temperature
            (city_id, time, tem_min, tem_max, tem_night, tem_eve, tem_morn) 
            VALUES ( ?, ?, ?, ?, ?, ?, ?)'''
    
    def __init__(self, city_id, dic_temp):
        self.city_id = city_id
        self.dic_temp = dic_temp
    
    def tempInfo(self):

        tem_min = round(self.dic_temp['temp_min'] - 273.15,2)
        tem_max = round(self.dic_temp['temp_max'] - 273.15,2)
        tem_night = round(self.dic_temp['temp_night'] - 273.15,2)
        tem_eve = round(self.dic_temp['temp_eve'] - 273.15,2)
        tem_morn = round(self.dic_temp['temp_morn'] - 273.15,2)
        time = datetime.fromtimestamp(self.dic_temp['dt'])

        return self.sql, (self.city_id, time, tem_min, tem_max, tem_night, tem_eve, tem_morn )
    
    def __dir__(self):
        return ['city_id', 'dic_temp', 'tempInfo()']  

    def __str__(self):
        return 'tempTable'
 

class Reunite:
    def __init__(self, dic_city):
        self.country = CountryInsert(dic_city['city']['country'])
        self.city = CityInsert(dic_city['city'])
        self.temp = [TempInsert(dic_city['city']['id'], x) for x in dic_city['data']]
        
    def __dir__(self):
        return self.__dict__.keys()  

    def __str__(self):
        return 'database' 
        
class Database:
    
    def __init__(self, data):
        self.data = [Reunite(x) for x in data]
    
    def script(self):
        
        return   '''DROP TABLE IF EXISTS Country;
                    DROP TABLE IF EXISTS City;
                    DROP TABLE IF EXISTS Temperature;

                    CREATE TABLE Country (
                        id             INTEGER PRIMARY KEY UNIQUE,
                        country_code   TEXT UNIQUE
                    );


                    CREATE TABLE City (
                        id             INTEGER PRIMARY KEY UNIQUE,
                        city_name      TEXT,
                        country_id     INTEGER,
                        latitude       FLOAT,
                        longitude      FLOAT

                    );

                    CREATE TABLE Temperature (
                        city_id     INTEGER,
                        time        INTEGER,
                        tem_min     FLOAT,
                        tem_max     FLOAT,
                        tem_night   FLOAT,
                        tem_eve     FLOAT,
                        tem_morn    FLOAT
                    )'''
 
    
    def __dir__(self):
        return ['data', 'script']    

    def __str__(self):
        return 'dailytoSQLite'