from aip import AipOcr
import json

#AipOcr是OCR的Python SDK客户端，为使用OCR的开发人员提供了一系列的交互方法。

APP_ID = 'you APP_ID'
API_KEY = 'you API_KEY'
SECRET_KEY = 'you SECRET_KEY'

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
