# -*- coding: utf-8 -*-
import requests
import csv
import time
from bs4 import BeautifulSoup


url1="https://free-api.heweather.com/s6/weather/now?location=119.946502,31.872678&key=ec1ddac21a4541d1b2c6db24bf9461ff"         #实况天气api
request1 = requests.get(url1)
print(request1.json())
now_wea = request1.json()['HeWeather6'][0]
basic_now_wea = now_wea['basic']
update_now_wea = now_wea['update']
now_now_wea = now_wea['now']

print('当前地区：',str(basic_now_wea['cnty']),str(basic_now_wea['admin_area']),str(basic_now_wea['parent_city']),str(basic_now_wea['location']))
print('当前时间：',str(update_now_wea['loc']))
print("体感温度：",now_now_wea['fl'])
print("温度：",now_now_wea['tmp'])
print("天气状况描述：",now_now_wea['cond_txt'])
print("温度：",now_now_wea['tmp'])
print('风向：',now_now_wea['wind_dir'],now_now_wea['wind_deg'])
print('风力：',now_now_wea['wind_sc'])
print('风速(km/h)：',now_now_wea['wind_spd'])
print('相对湿度：',now_now_wea['hum'])
print('降水量：',now_now_wea['pcpn'])
print('大气压强：',now_now_wea['pres'])
print('能见度：',now_now_wea['vis'])
print('云量：',now_now_wea['cloud'])

f = open('hefeng_wea_rec.txt','a')
f.write('**********************************************\n')
f.write('当前地区：'+ str(basic_now_wea['cnty'])+ str(basic_now_wea['admin_area'])+ str(basic_now_wea['parent_city'])+ str(basic_now_wea['location'])+'\n')
f.write('当前时间：'+ str(update_now_wea['loc'])+'\n')
f.write("体感温度："+ str(now_now_wea['fl'])+'\n')
f.write("温度："+ str(now_now_wea['tmp'])+'\n')
f.write('风向：'+ str(now_now_wea['wind_dir']+now_now_wea['wind_deg'])+'\n')
f.write('风力：'+ str(now_now_wea['wind_sc'])+'\n')
f.write('风速(km/h)：'+ str(now_now_wea['wind_spd'])+'\n')
f.write('相对湿度：'+ str(now_now_wea['hum'])+'\n')
f.write('降水量：'+ str(now_now_wea['pcpn'])+'\n')
f.write('大气压强：'+ str(now_now_wea['pres'])+'\n')
f.write('能见度：'+ str(now_now_wea['vis'])+'\n')
f.write('云量：'+ str(now_now_wea['cloud'])+'\n')
f.close()