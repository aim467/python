from tkinter import *
import json
import requests


class Weather(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("天气查询")
        self.window.geometry('1200x900+100+100')

        self.label = Label(self.window, text="请输入你要查询的城市:", fg="blue", font="Arial 14")
        self.label.pack(side='top', pady=5)

        self.entry = Entry(self.window, width=25, font="Arial 14")
        self.entry.pack(side='top', pady=5)

        self.listbox = Listbox(self.window, font="Arial 9", width=120, height=40)
        self.listbox.pack()

        self.button = Button(self.window, text="点击查询", font="Arial 9", width=15, command=self.weather)
        self.button.pack(pady=10)

        # 打开city.json文件并且读取 用json.loads把文件流转化为dict类型
        self.text = open("city.json", "r")
        self.data = self.text.read()
        self.info = json.loads(self.data)

        self.window.mainloop()

    def weather(self):
        City = self.entry.get()
        City = str(City)
        # 获取城市 遍历self.data匹配和从键盘输入一样的城市 并且拿出城市代码
        for city in self.info:
            if City == city["city_name"]:
                City_code = city["city_code"]
                break

        url = "http://t.weather.sojson.com/api/weather/city/"
        r = requests.get(url + City_code)
        data = json.loads(r.text)
        msg = data["data"]["forecast"]
        msg.reverse()
    
        for b in msg:
            # print("\n")
            self.listbox.insert(0,"\n")
            for c,d in b.items():
                # print(c+"\t",d)
                f = str(c)+": "+str(d)
                self.listbox.insert(0,f)
                
        

test = Weather()

