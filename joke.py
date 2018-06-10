import requests
import json
import sys
from random import randint

def joke(maxResult,page):
    url = "https://route.showapi.com/341-1?maxResult="+maxResult+"&page="+page+"&showapi_appid=65995&&showapi_sign=de43c43d64da42d4a69316b6a7673907"

    response = requests.get(url)
    data = response.json()["showapi_res_body"]["contentlist"]
    print("\n")
    for joke in data:
        print("标题:   "+joke["title"])
        text = joke["text"]
        msg = text.strip('\n')
        print(msg)
        print("\n")

if __name__ == '__main__':
    print("-----------------------")
    print("  欢迎进入笑话大全系统    ")
    print("-----------------------")
    number = int(input("请选择你要获取笑话的方式:"))
    print("1方式为随机笑话")
    print("2方式为手动操作")
    if number == 1:
        maxResult = randint(1,50)
        page = randint(1,1000)
        date = joke(str(maxResult),str(page))
        print(date)
    elif number == 2:
        maxResult = input("请输入你想显示的笑话数量(最大为50):")
        page = input("请输入你要获取的页数:")
        date = joke(str(maxResult),str(page))
        print(date)
