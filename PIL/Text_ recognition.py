# import requests
# import json
# import base64

# API_KEY = 'SKAzSnndIqAYlT5nEo350gLW'
# SECRET_KEY = 'EsUyiCgHnK7hZlQTg6jAAZyuPNsLm1Hi'

# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
# # headers = {'Content-Type':'application/json; charset=UTF-8'}
# response = requests.get(host)
# date = json.loads(response.text)
# access_token = date['access_token']

# url='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token='+access_token
# # print(url)
# f = open('/home/aim/Download/test.jpg','rb')

# img = base64.b64decode(f.read())
# paylod = {"image":img}
# params = requests.urllib3.request.urlencode(paylod)
# headers = {'Content-Type':'application/x-www-form-urlencoded'}
# data = requests.get(url,params=params,headers=headers)
# print(data.status_code)
# print(data.text)


#AipOcr是OCR的Python SDK客户端，为使用OCR的开发人员提供了一系列的交互方法。
from aip import AipOcr
import json
APP_ID = '11666108'
API_KEY = 'SKAzSnndIqAYlT5nEo350gLW'
SECRET_KEY = 'EsUyiCgHnK7hZlQTg6jAAZyuPNsLm1Hi'

aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

file_path = '/home/aim/Download/test.jpg'
#参数设置
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(file_path), options)
print(result['words_result'][0]['words'])

