import requests
import json

cityname = input("请输入你要查询的城市名:")

url = 'https://www.sojson.com/open/api/weather/json.shtml?city='+cityname

data = requests.get(url)
'''
data.json
city = data.json()["city"]
wendu = data.json()["data"]["wendu"]
wuran = data.json()["data"]["quality"]

print("你所查询的城市为:"+city)
print("你所查询的城市今天的温度为:"+wendu+"℃")
print("污染级数为:"+wuran)
'''
date = data.json()["data"]["forecast"]

from tabulate import tabulate
for dict1 in date[:4]:
    dict2 = dict1.keys()
    dict3 = dict1.values()
    list = []
    list.append(dict2)
    list.append(dict3)
    print(tabulate(list,tablefmt='grid'))   
