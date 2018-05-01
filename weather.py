

#coding='utf-8'

from city import city
import requests
import json

cityname = input("请输入你要查询的天气:")
citycode = city[cityname]


url =  "http://www.weather.com.cn/data/sk/"+citycode+".html" 
content = requests.get(url)
content.encoding = 'utf-8'
city = content.json()["weatherinfo"]["city"]
wendu = content.json()["weatherinfo"]["temp"]
print("城市:",city,"温度:",wendu)
