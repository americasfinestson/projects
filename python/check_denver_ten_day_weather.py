#!/usr/bin/env python3

""" Scrapes 9news.com to gather the 10-day weather forecast for Denver.

Usage:

    python3 check_denver_ten_day_weather.py

Arguments: None

"""

import requests_html


def main():

    response = requests_html.HTMLSession().get('https://9news.com/weather')
    ten_day_weather_container = response.html.find('div.weather-10-day', first=True)
    daily_weather = ten_day_weather_container.find('div.weather-10-day__row')

    for d in daily_weather:

        high_temp = d.find('div.weather-10-day__temperature-high', first=True)
        date = d.find('span.weather-10-day__date.weather-10-day__date_visible_true', first=True)
        print("For " + date.text + ", the daily high temperature is " + high_temp.text)


if __name__ == '__main__':

    main()

