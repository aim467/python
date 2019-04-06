from tkinter import *
import requests
from bs4 import BeautifulSoup
import json


class Fration(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("IP查询")
        self.root.geometry('800x500')
        self.root.geometry('+400+300')

        self.input = Entry(self.root, width=30, font="宋体 13")
        self.input.pack(pady=10)

        self.text = Text(self.root, show=None, width=60, height=8, font="宋体 10")
        self.text.pack(padx=10, pady=10)

        self.button = Button(self.root, command=self.ip_search, text="点击查询", font="宋体 15")
        self.button.pack()

        # self.var = StringVar()
        
        self.root.mainloop()

    def ip_search(self):
        var = self.input.get()
        # data = {
        #     "ip": var
        # }
        # r = requests.get("https://www.ip.cn/index.php?", params=data)
        # html = BeautifulSoup(r.text, "html.parser")
        # html = html.text.strip().replace("\n", "")
        # var = str(html)
        # self.text.insert('insert', var)
        url = "https://tool.lu/ip/ajax.html"

        headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        parmars = {
            "ip": var
            }
        r = requests.post(url, data=parmars, headers=headers)
        data = json.loads(r.text)

        ip = data["text"]["ip"]
        ip_long = data["text"]["l"]
        location = data["text"]["location"]
        ipip_location = data["text"]["ipip_location"]
        tb_location = data["text"]["tb_location"]
        ip2region_location = data["text"]["ip2region_location"]

        self.text.insert('insert', "ip: " + str(ip)+"\n")
        self.text.insert('insert', "ip长度: " + str(ip_long)+"\n")
        self.text.insert('insert', "归属地: " + str(location)+"\n")
        self.text.insert('insert', "归属地ipip: " + str(ipip_location)+"\n")
        self.text.insert('insert', "淘宝数据归属地: " + str(tb_location)+"\n")
        self.text.insert('insert', "ip2归属地: " + str(ip2region_location)+"\n")


         

if __name__ == "__main__":
    ipInfo = Fration()

# root = Tk()
# root.title("ip查询")
# root.geometry('800x600')

# var = StringVar()

# input = Entry(root, width=20)
# input.pack()

# text = Text(root, show=None, height=8, width=80)
# text.pack()

# def ip_search():
#     ip = input.get()
#     ip = str(ip)
#     data = {
#         "ip": ip
#     }
#         # r = requests.get("https://www.ip.cn/index.php?ip="+ip)
#     r = requests.get("https://www.ip.cn/index.php?", params=data)

#     html = r.text
#     html = BeautifulSoup(html, "html.parser")
#     html = html.text.strip().replace("\n", "")
#     # html = str(html)
#     global var
#     var = str(html)
#     text.insert('insert', var)

# button = Button(root, command=ip_search, text="点击查询", width=20, height=4)
# button.pack()

# root.mainloop()




