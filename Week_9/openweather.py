# coding: utf-8
import requests 
from typing import Dict, Any
# def current_weather(id, coord = {'lat': 49.273901, 'lon' : -123.002100}):
#     """
#     Function receives: 
#      - id: API key
#      - coord: a dictionary containing the longitude and latitude of the city.

#     The function returns:
#      - current weather data
#     """

#     serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'
#     parms ='lat=%g&lon=%g&units=metric&appid=%s' %(coord['lat'], coord['lon'],id) #Parameters
#     url = serviceurl + parms
    
#     response = requests.get(url)
#     response.raise_for_status()

#     return response.text

def current_weather(api_key: str, coord: Dict[str, float] = {'lat': 49.273901, 'lon': -123.002100}) -> Dict[str, Any]:
    """
    Fetches current weather data from OpenWeatherMap API.

    Parameters:
    - api_key (str): Your OpenWeatherMap API key.
    - coord (dict): Dictionary with 'lat' and 'lon' keys for coordinates.

    Returns:
    - dict: Parsed JSON response containing current weather data.
    """
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': coord['lat'],
        'lon': coord['lon'],
        'units': 'metric',
        'appid': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}


# def air_pollution(id, coord = {'lat': 49.273901, 'lon' : -123.002100}):
#     """
#     Function receives: 
#      - id: API key
#      - coord: a dictionary containing the longitude and latitude of the city.

#     The function returns:
#      - Forecast and historical air pollution data for any coordinates on the globe
#     """

#     serviceurl = 'https://api.openweathermap.org/data/2.5/air_pollution?'
#     parms ='lat=%g&lon=%g&units=metric&appid=%s' %(coord['lat'], coord['lon'],id) #Parameters
#     url = serviceurl + parms
    
#     response = requests.get(url)
#     response.raise_for_status()

#     return response.text

def air_pollution(api_key: str, coord: Dict[str, float] = {'lat': 49.273901, 'lon': -123.002100}) -> Dict[str, Any]:
    """
    Fetches current air pollution data from OpenWeatherMap API.

    Parameters:
    - api_key (str): Your OpenWeatherMap API key.
    - coord (dict): Dictionary with 'lat' and 'lon' keys for coordinates.

    Returns:
    - dict: Parsed JSON response containing air pollution data.
    """
    url = 'https://api.openweathermap.org/data/2.5/air_pollution'
    params = {
        'lat': coord['lat'],
        'lon': coord['lon'],
        'appid': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching air pollution data: {e}")
        return {}

    