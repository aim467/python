import json,requests
from pprint import pprint


def phone_search(phone):
    url = 'http://api.k780.com/?app=phone.get&phone='+phone+'&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'

    data = requests.get(url)
    print("-----查询中----")
    if data.status_code == 200:
        print("状态码为:",data.status_code)
        print("查询成功!")
    else:
        print("查询出错")
    date = data.json()["result"]
    print("你所查询的电话号码为:"+date["phone"])
    print("所在城市为:"+date["att"])

if __name__ == '__main__':
    phone = input("请输入你要查询的电话号码:")
    phone_search(phone)