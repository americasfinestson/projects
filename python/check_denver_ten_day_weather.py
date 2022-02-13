#!/usr/bin/env python3

""" Scrapes 9news.com to gather the 10-day weather forecast for Denver.

Usage:

    python3 check_denver_ten_day_weather.py

Arguments: None

"""

import requests_html
from pprint import pprint


class Weather():

    def __init__(self,
                 url='http://9news.com/weather',
                 weather_container_css_selector='div.weather-10-day',
                 daily_weather_css_selector='div.weather-10-day__row',
                 daily_weather_high_temp_css_selector='div.weather-10-day__temperature-high',
                 daily_weather_low_temp_css_selector='div.weather-10-day__temperature-low',
                 daily_weather_date_css_selector='span.weather-10-day__date.weather-10-day__date_visible_true'):
        self.url = url
        self.weather_container_css_selector = weather_container_css_selector
        self.daily_weather_css_selector = daily_weather_css_selector
        self.daily_weather_high_temp_css_selector = daily_weather_high_temp_css_selector
        self.daily_weather_low_temp_css_selector = daily_weather_low_temp_css_selector
        self.daily_weather_date_css_selector = daily_weather_date_css_selector

    def get_content(self):
        response_full = requests_html.HTMLSession().get(self.url)
        return response_full

    def get_weather_forecast(self):
        response_full = self.get_content()

        weather_container_full_str = str(self.weather_container_css_selector)
        daily_weather_str = str(self.daily_weather_css_selector)

        weather_container_full = response_full.html.find(weather_container_full_str, first=True)
        daily_weather = weather_container_full.find(daily_weather_str)
        daily_weather_forecast = []

        for d in daily_weather:
            date = d.find(self.daily_weather_date_css_selector, first=True)
            high_temp = d.find(self.daily_weather_high_temp_css_selector, first=True)
            low_temp = d.find(self.daily_weather_low_temp_css_selector, first=True)
            daily_weather_forecast.append(str(date) + ': High of ' + str(high_temp) + ' and a low of ' + str(low_temp))
        return daily_weather_forecast


def main():

    weather_9_news = Weather()
    pprint(weather_9_news.get_weather_forecast())

#    response = requests_html.HTMLSession().get('https://9news.com/weather')
#    ten_day_weather_container = response.html.find('div.weather-10-day', first=True)
#    daily_weather = ten_day_weather_container.find('div.weather-10-day__row')
#
#    for d in daily_weather:
#
#        high_temp = d.find('div.weather-10-day__temperature-high', first=True)
#        date = d.find('span.weather-10-day__date.weather-10-day__date_visible_true', first=True)
#        print("For " + date.text + ", the daily high temperature is " + high_temp.text)


if __name__ == '__main__':

    main()

