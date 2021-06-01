from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, flash, redirect, request, abort
import requests

app = Flask(__name__)
app.secret_key = "Secret Key"


@app.route('/')
def home():
    return render_template('weather_design.html')


@app.route('/update_api', methods=['GET', 'POST'])
def update_api():
    if request.method == 'POST':
        city_name_1 = request.form.get('city_name_1')
        city_name_2 = request.form.get('city_name_2')
        city_name_3 = request.form.get('city_name_3')
        api_key = '402462616a6745b49281a2d972552f90'
        getting_data_from_api_city_1 = 'https://api.weatherbit.io/v2.0/forecast/daily?city=' + \
            city_name_1 + '&key=' + api_key
        city_1_hourly_weather='http://api.weatherapi.com/v1/forecast.json?key=efe20f3c9a6f460cab691218211305&q='+ city_name_1 +'&days=1&aqi=no&alerts=no'
        city_1_hourly_weather_data=requests.get(city_1_hourly_weather)
        city_1_hourly_weather_data_json=city_1_hourly_weather_data.json()
        city_1_time_00_AM = "{:.2f}".format(city_1_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][0]['temp_c'])
        city_1_time_06_AM = "{:.2f}".format(city_1_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][5]['temp_c'])
        city_1_time_12_NOON = "{:.2f}".format(city_1_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][11]['temp_c'])
        city_1_time_06_PM = "{:.2f}".format(city_1_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][17]['temp_c'])
        response_city_1 = requests.get(getting_data_from_api_city_1)
        data_convert_to_json_city_1 = response_city_1.json()
        city_1_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][0]['min_temp'])
        city_1_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][0]['max_temp'])
        city_1_weather_desc = data_convert_to_json_city_1['data'][0]['weather']['description']
        city_1_weather_icon = data_convert_to_json_city_1['data'][0]['weather']['icon'][1:]
        city_1_temp = "{:.2f}".format(
            data_convert_to_json_city_1['data'][0]['temp'])
        city_1_day_2_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][1]['min_temp'])
        city_1_day_2_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][1]['max_temp'])
        city_1_day_2_weather_icon = data_convert_to_json_city_1['data'][1]['weather']['icon'][1:]
        city_1_day_3_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][2]['min_temp'])
        city_1_day_3_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][2]['max_temp'])
        city_1_day_3_weather_icon = data_convert_to_json_city_1['data'][2]['weather']['icon'][1:]
        city_1_day_4_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][3]['min_temp'])
        city_1_day_4_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][3]['max_temp'])
        city_1_day_4_weather_icon = data_convert_to_json_city_1['data'][3]['weather']['icon'][1:]
        city_1_day_5_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][4]['min_temp'])
        city_1_day_5_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][4]['max_temp'])
        city_1_day_5_weather_icon = data_convert_to_json_city_1['data'][4]['weather']['icon'][1:]
        city_1_day_6_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][6]['min_temp'])
        city_1_day_6_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][6]['max_temp'])
        city_1_day_6_weather_icon = data_convert_to_json_city_1['data'][6]['weather']['icon'][1:]
        city_1_day_7_temp_min = "{:.0f}".format(
            data_convert_to_json_city_1['data'][7]['min_temp'])
        city_1_day_7_temp_max = "{:.0f}".format(
            data_convert_to_json_city_1['data'][7]['max_temp'])
        city_1_day_7_weather_icon = data_convert_to_json_city_1['data'][7]['weather']['icon'][1:]
        if city_name_2:
            city_2_hourly_weather='http://api.weatherapi.com/v1/forecast.json?key=efe20f3c9a6f460cab691218211305&q='+ city_name_2 +'&days=1&aqi=no&alerts=no'
            city_2_hourly_weather_data=requests.get(city_2_hourly_weather)
            city_2_hourly_weather_data_json=city_2_hourly_weather_data.json()
            city_2_time_00_AM = "{:.2f}".format(city_2_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][0]['temp_c'])
            city_2_time_06_AM = "{:.2f}".format(city_2_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][5]['temp_c'])
            city_2_time_12_NOON = "{:.2f}".format(city_2_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][11]['temp_c'])
            city_2_time_06_PM = "{:.2f}".format(city_2_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][17]['temp_c'])
            getting_data_from_api_city_2 = 'https://api.weatherbit.io/v2.0/forecast/daily?city=' + \
                city_name_2 + '&key=' + api_key
            getting_data_from_api_city_3 = 'https://api.weatherbit.io/v2.0/forecast/daily?city=' + \
                city_name_3 + '&key=' + api_key
            response_city_2 = requests.get(getting_data_from_api_city_2)
            response_city_3 = requests.get(getting_data_from_api_city_3)
            data_convert_to_json_city_2 = response_city_2.json()
            data_convert_to_json_city_3 = response_city_3.json()
            # city 2
            city_2_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][0]['min_temp'])
            city_2_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][0]['max_temp'])
            city_2_weather_desc = data_convert_to_json_city_2['data'][0]['weather']['description']
            city_2_weather_icon = data_convert_to_json_city_2['data'][0]['weather']['icon'][1:]
            city_2_temp = "{:.2f}".format(
                data_convert_to_json_city_2['data'][0]['temp'])
            city_2_day_2_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][1]['min_temp'])
            city_2_day_2_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][1]['max_temp'])
            city_2_day_2_weather_icon = data_convert_to_json_city_2['data'][1]['weather']['icon'][1:]
            city_2_day_3_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][2]['min_temp'])
            city_2_day_3_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][2]['max_temp'])
            city_2_day_3_weather_icon = data_convert_to_json_city_2['data'][2]['weather']['icon'][1:]
            city_2_day_4_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][3]['min_temp'])
            city_2_day_4_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][3]['max_temp'])
            city_2_day_4_weather_icon = data_convert_to_json_city_2['data'][3]['weather']['icon'][1:]
            city_2_day_5_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][4]['min_temp'])
            city_2_day_5_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][4]['max_temp'])
            city_2_day_5_weather_icon = data_convert_to_json_city_2['data'][4]['weather']['icon'][1:]
            city_2_day_6_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][6]['min_temp'])
            city_2_day_6_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][6]['max_temp'])
            city_2_day_6_weather_icon = data_convert_to_json_city_2['data'][6]['weather']['icon'][1:]
            city_2_day_7_temp_min = "{:.0f}".format(
                data_convert_to_json_city_2['data'][7]['min_temp'])
            city_2_day_7_temp_max = "{:.0f}".format(
                data_convert_to_json_city_2['data'][7]['max_temp'])
            city_2_day_7_weather_icon = data_convert_to_json_city_2['data'][7]['weather']['icon'][1:]

            if city_name_3:
                # city 3
                city_3_hourly_weather='http://api.weatherapi.com/v1/forecast.json?key=efe20f3c9a6f460cab691218211305&q='+ city_name_3 +'&days=1&aqi=no&alerts=no'
                city_3_hourly_weather_data=requests.get(city_3_hourly_weather)
                city_3_hourly_weather_data_json=city_3_hourly_weather_data.json()
                city_3_time_00_AM = "{:.2f}".format(city_3_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][0]['temp_c'])
                city_3_time_06_AM = "{:.2f}".format(city_3_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][5]['temp_c'])
                city_3_time_12_NOON = "{:.2f}".format(city_3_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][11]['temp_c'])
                city_3_time_06_PM = "{:.2f}".format(city_3_hourly_weather_data_json['forecast']['forecastday'][0]['hour'][17]['temp_c'])
                city_3_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][0]['min_temp'])
                city_3_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][0]['max_temp'])
                city_3_weather_desc = data_convert_to_json_city_3['data'][0]['weather']['description']
                city_3_weather_icon = data_convert_to_json_city_3['data'][0]['weather']['icon'][1:]
                city_3_temp = "{:.2f}".format(
                    data_convert_to_json_city_3['data'][0]['temp'])
                city_3_day_2_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][1]['min_temp'])
                city_3_day_2_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][1]['max_temp'])
                city_3_day_2_weather_icon = data_convert_to_json_city_3[
                    'data'][1]['weather']['icon'][1:]
                city_3_day_3_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][2]['min_temp'])
                city_3_day_3_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][2]['max_temp'])
                city_3_day_3_weather_icon = data_convert_to_json_city_3[
                    'data'][2]['weather']['icon'][1:]
                city_3_day_4_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][3]['min_temp'])
                city_3_day_4_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][3]['max_temp'])
                city_3_day_4_weather_icon = data_convert_to_json_city_3[
                    'data'][3]['weather']['icon'][1:]
                city_3_day_5_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][4]['min_temp'])
                city_3_day_5_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][4]['max_temp'])
                city_3_day_5_weather_icon = data_convert_to_json_city_3[
                    'data'][4]['weather']['icon'][1:]
                city_3_day_6_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][6]['min_temp'])
                city_3_day_6_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][6]['max_temp'])
                city_3_day_6_weather_icon = data_convert_to_json_city_3[
                    'data'][6]['weather']['icon'][1:]
                city_3_day_7_temp_min = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][7]['min_temp'])
                city_3_day_7_temp_max = "{:.0f}".format(
                    data_convert_to_json_city_3['data'][7]['max_temp'])
                city_3_day_7_weather_icon = data_convert_to_json_city_3[
                    'data'][7]['weather']['icon'][1:]
                return render_template('weather_design.html', city_3_time_06_PM=city_3_time_06_PM, city_3_time_12_NOON=city_3_time_12_NOON, city_3_time_06_AM=city_3_time_06_AM, city_3_time_00_AM=city_3_time_00_AM, city_1_time_06_PM=city_1_time_06_PM, city_1_time_12_NOON=city_1_time_12_NOON, city_1_time_06_AM=city_1_time_06_AM, city_1_time_00_AM=city_1_time_00_AM, city_2_time_06_PM=city_2_time_06_PM, city_2_time_12_NOON=city_2_time_12_NOON, city_2_time_06_AM=city_2_time_06_AM, city_2_time_00_AM=city_2_time_00_AM, city_name_1=request.form.get('city_name_1'), city_1_temp_min=city_1_temp_min, city_1_temp_max=city_1_temp_max, city_1_weather_desc=city_1_weather_desc, city_1_weather_icon=city_1_weather_icon, city_1_temp=city_1_temp, city_1_day_2_temp_min=city_1_day_2_temp_min, city_1_day_2_temp_max=city_1_day_2_temp_max, city_1_day_2_weather_icon=city_1_day_2_weather_icon, city_1_day_3_temp_min=city_1_day_3_temp_min, city_1_day_3_temp_max=city_1_day_3_temp_max, city_1_day_3_weather_icon=city_1_day_3_weather_icon, city_1_day_4_temp_min=city_1_day_4_temp_min, city_1_day_4_temp_max=city_1_day_4_temp_max, city_1_day_4_weather_icon=city_1_day_4_weather_icon, city_1_day_5_temp_min=city_1_day_5_temp_min, city_1_day_5_temp_max=city_1_day_5_temp_max, city_1_day_5_weather_icon=city_1_day_5_weather_icon, city_1_day_6_temp_min=city_1_day_6_temp_min, city_1_day_6_temp_max=city_1_day_6_temp_max, city_1_day_6_weather_icon=city_1_day_6_weather_icon, city_1_day_7_temp_min=city_1_day_7_temp_min, city_1_day_7_temp_max=city_1_day_7_temp_max, city_1_day_7_weather_icon=city_1_day_7_weather_icon, city_name_2=request.form.get('city_name_2'), city_2_temp_min=city_2_temp_min, city_2_temp_max=city_2_temp_max, city_2_weather_desc=city_2_weather_desc, city_2_weather_icon=city_2_weather_icon, city_2_temp=city_2_temp, city_2_day_2_temp_min=city_2_day_2_temp_min, city_2_day_2_temp_max=city_2_day_2_temp_max, city_2_day_2_weather_icon=city_2_day_2_weather_icon, city_2_day_3_temp_min=city_2_day_3_temp_min, city_2_day_3_temp_max=city_2_day_3_temp_max, city_2_day_3_weather_icon=city_2_day_3_weather_icon, city_2_day_4_temp_min=city_2_day_4_temp_min, city_2_day_4_temp_max=city_2_day_4_temp_max, city_2_day_4_weather_icon=city_2_day_4_weather_icon, city_2_day_5_temp_min=city_2_day_5_temp_min, city_2_day_5_temp_max=city_2_day_5_temp_max, city_2_day_5_weather_icon=city_2_day_5_weather_icon, city_2_day_6_temp_min=city_2_day_6_temp_min, city_2_day_6_temp_max=city_2_day_6_temp_max, city_2_day_6_weather_icon=city_2_day_6_weather_icon, city_2_day_7_temp_min=city_2_day_7_temp_min, city_2_day_7_temp_max=city_2_day_7_temp_max, city_2_day_7_weather_icon=city_2_day_7_weather_icon, city_name_3=request.form.get('city_name_3'), city_3_temp_min=city_3_temp_min, city_3_temp_max=city_3_temp_max, city_3_weather_desc=city_3_weather_desc, city_3_weather_icon=city_3_weather_icon, city_3_temp=city_3_temp, city_3_day_2_temp_min=city_3_day_2_temp_min, city_3_day_2_temp_max=city_3_day_2_temp_max, city_3_day_2_weather_icon=city_3_day_2_weather_icon, city_3_day_3_temp_min=city_3_day_3_temp_min, city_3_day_3_temp_max=city_3_day_3_temp_max, city_3_day_3_weather_icon=city_3_day_3_weather_icon, city_3_day_4_temp_min=city_3_day_4_temp_min, city_3_day_4_temp_max=city_3_day_4_temp_max, city_3_day_4_weather_icon=city_3_day_4_weather_icon, city_3_day_5_temp_min=city_3_day_5_temp_min, city_3_day_5_temp_max=city_3_day_5_temp_max, city_3_day_5_weather_icon=city_3_day_5_weather_icon, city_3_day_6_temp_min=city_3_day_6_temp_min, city_3_day_6_temp_max=city_3_day_6_temp_max, city_3_day_6_weather_icon=city_3_day_6_weather_icon, city_3_day_7_temp_min=city_3_day_7_temp_min, city_3_day_7_temp_max=city_3_day_7_temp_max, city_3_day_7_weather_icon=city_3_day_7_weather_icon)
            return render_template('weather_design.html', city_1_time_06_PM=city_1_time_06_PM, city_1_time_12_NOON=city_1_time_12_NOON, city_1_time_06_AM=city_1_time_06_AM, city_1_time_00_AM=city_1_time_00_AM, city_2_time_06_PM=city_2_time_06_PM, city_2_time_12_NOON=city_2_time_12_NOON, city_2_time_06_AM=city_2_time_06_AM, city_2_time_00_AM=city_2_time_00_AM, city_name_1=request.form.get('city_name_1'), city_1_temp_min=city_1_temp_min, city_1_temp_max=city_1_temp_max, city_1_weather_desc=city_1_weather_desc, city_1_weather_icon=city_1_weather_icon, city_1_temp=city_1_temp, city_1_day_2_temp_min=city_1_day_2_temp_min, city_1_day_2_temp_max=city_1_day_2_temp_max, city_1_day_2_weather_icon=city_1_day_2_weather_icon, city_1_day_3_temp_min=city_1_day_3_temp_min, city_1_day_3_temp_max=city_1_day_3_temp_max, city_1_day_3_weather_icon=city_1_day_3_weather_icon, city_1_day_4_temp_min=city_1_day_4_temp_min, city_1_day_4_temp_max=city_1_day_4_temp_max, city_1_day_4_weather_icon=city_1_day_4_weather_icon, city_1_day_5_temp_min=city_1_day_5_temp_min, city_1_day_5_temp_max=city_1_day_5_temp_max, city_1_day_5_weather_icon=city_1_day_5_weather_icon, city_1_day_6_temp_min=city_1_day_6_temp_min, city_1_day_6_temp_max=city_1_day_6_temp_max, city_1_day_6_weather_icon=city_1_day_6_weather_icon, city_1_day_7_temp_min=city_1_day_7_temp_min, city_1_day_7_temp_max=city_1_day_7_temp_max, city_1_day_7_weather_icon=city_1_day_7_weather_icon, city_name_2=request.form.get('city_name_2'), city_2_temp_min=city_2_temp_min, city_2_temp_max=city_2_temp_max, city_2_weather_desc=city_2_weather_desc, city_2_weather_icon=city_2_weather_icon, city_2_temp=city_2_temp, city_2_day_2_temp_min=city_2_day_2_temp_min, city_2_day_2_temp_max=city_2_day_2_temp_max, city_2_day_2_weather_icon=city_2_day_2_weather_icon, city_2_day_3_temp_min=city_2_day_3_temp_min, city_2_day_3_temp_max=city_2_day_3_temp_max, city_2_day_3_weather_icon=city_2_day_3_weather_icon, city_2_day_4_temp_min=city_2_day_4_temp_min, city_2_day_4_temp_max=city_2_day_4_temp_max, city_2_day_4_weather_icon=city_2_day_4_weather_icon, city_2_day_5_temp_min=city_2_day_5_temp_min, city_2_day_5_temp_max=city_2_day_5_temp_max, city_2_day_5_weather_icon=city_2_day_5_weather_icon, city_2_day_6_temp_min=city_2_day_6_temp_min, city_2_day_6_temp_max=city_2_day_6_temp_max, city_2_day_6_weather_icon=city_2_day_6_weather_icon, city_2_day_7_temp_min=city_2_day_7_temp_min, city_2_day_7_temp_max=city_2_day_7_temp_max, city_2_day_7_weather_icon=city_2_day_7_weather_icon)
        return render_template('weather_design.html', city_1_time_06_PM=city_1_time_06_PM, city_1_time_12_NOON=city_1_time_12_NOON, city_1_time_06_AM=city_1_time_06_AM, city_1_time_00_AM=city_1_time_00_AM, city_name_1=request.form.get('city_name_1'), city_1_temp_min=city_1_temp_min, city_1_temp_max=city_1_temp_max, city_1_weather_desc=city_1_weather_desc, city_1_weather_icon=city_1_weather_icon, city_1_temp=city_1_temp, city_1_day_2_temp_min=city_1_day_2_temp_min, city_1_day_2_temp_max=city_1_day_2_temp_max, city_1_day_2_weather_icon=city_1_day_2_weather_icon, city_1_day_3_temp_min=city_1_day_3_temp_min, city_1_day_3_temp_max=city_1_day_3_temp_max, city_1_day_3_weather_icon=city_1_day_3_weather_icon, city_1_day_4_temp_min=city_1_day_4_temp_min, city_1_day_4_temp_max=city_1_day_4_temp_max, city_1_day_4_weather_icon=city_1_day_4_weather_icon, city_1_day_5_temp_min=city_1_day_5_temp_min, city_1_day_5_temp_max=city_1_day_5_temp_max, city_1_day_5_weather_icon=city_1_day_5_weather_icon, city_1_day_6_temp_min=city_1_day_6_temp_min, city_1_day_6_temp_max=city_1_day_6_temp_max, city_1_day_6_weather_icon=city_1_day_6_weather_icon, city_1_day_7_temp_min=city_1_day_7_temp_min, city_1_day_7_temp_max=city_1_day_7_temp_max, city_1_day_7_weather_icon=city_1_day_7_weather_icon)
    return render_template('weather_design.html')


if __name__ == '__main__':
    app.run(debug=True)
