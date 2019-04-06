from tkinter import *
import requests
import json


class Express(object):
    def __init__(self):
        """
        初始化窗口控件
        """
        self.windows = Tk()
        self.windows.title("快递查询")
        self.windows.geometry("800x600+500+600")

        self.label1 = Label(self.windows, text="请输入快递公司:", font="华文行楷 15", width=30)
        self.label1.pack(side='top')
        self.entry1 = Entry(self.windows, width=30, font="None 15")
        self.entry1.pack(padx=15, pady=10)

        self.label2 = Label(self.windows, text="请输入快递编号:", font="Arial 15", width=30)
        self.label2.pack(side='top')
        self.entry2 = Entry(self.windows, width=30, font="None 15")
        self.entry2.pack(padx=15, pady=10)

        self.listbox = Listbox(self.windows,width=75, font="None 10", )
        self.listbox.pack()

        self.button = Button(self.windows, text="点击查询快递信息", command=self.get_express, width=15, font="Arial 10")
        self.button.pack(pady=10)

        self.windows.mainloop()

    def get_express(self):
        """
        从两个输入框获取 快递单号和快递公司信息
        然后调用api接口
        """
        var1 = self.entry1.get()
        var2 = self.entry2.get()

        url = "https://www.kuaidi100.com/query?type="+str(var1)+"&postid="+str(var2)
        res = requests.get(url)

        html = json.loads(res.text)

        Data = html["data"]

        for data in Data:
            self.listbox.insert(0, data["ftime"])
            self.listbox.insert(1, data["context"])
 

if __name__ == "__main__":
    express = Express()
