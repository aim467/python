import requests
import json


input_ip = input("请输入你要查询的ip:")

    
url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+input_ip
data = requests.get(url)
#print(data.status_code)
#print(data.encoding)

ip = data.json()["data"]["ip"]
isp = data.json()["data"]["isp"]
country = data.json()["data"]["country"]
city = data.json()["data"]["city"]

print("你所查询的ip为:"+ip)
print("你所查询的ip的服务商为:"+isp)
print("你所查询的ip的国家为:"+country)
print("你所查询的ip的城市为:"+city)  