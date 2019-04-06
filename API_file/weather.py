import requests
import json


def weather(cityname):
    url = 'https://www.sojson.com/open/api/weather/json.shtml?city='+cityname
    weather_data = requests.get(url)


    data = weather_data.json()["data"]["forecast"]
    from tabulate import tabulate
    for dict1 in data[:4]:
        dict2 = dict1.keys()
        dict3 = dict1.values()
        list = []
        list.append(dict2)
        list.append(dict3)
        print(tabulate(list,tablefmt='grid'))
        print('\n')   

if __name__ == '__main__':
    cityname = input("请输入你要查询的城市名:")
    weather(str(cityname))