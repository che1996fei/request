import requests
import re

#基本实例
data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)

#抓取网页
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('<a class="question_link" href=.*? target="_blank" data-id=.*? data-za-element-name="Title">(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
print(title)

#抓取二进制数据
r = requests.get('https://github.com/favicon.ico')
with open('favcion.ico', 'wb') as f:
    f.write(r.content)

#Cookies
headers = {
    'Cookies': '_xsrf=1w8MZO6m1JZ6EqCDDXOz7tlj5Ei4D9a1; _zap=c12f5d09-8759-4620-a3be-4ba98724cc7c; d_c0="AIBlODm8PQ-PToMlt3c2cBZNHlTBCyS_Cgc=|1554621020"; capsion_ticket="2|1:0|10:1554621031|14:capsion_ticket|44:YjE0M2IzYTc4MDJiNDFkOWEyZTRhMWFiZTg5MWY0MjU=|ae390b0ac163de6d709f42e99c255bdfd7ff13ec177b6e8f6de2a7e045ef3dc1"; z_c0="2|1:0|10:1554621078|4:z_c0|92:Mi4xWTUtYkNRQUFBQUFBZ0dVNE9idzlEeWNBQUFDRUFsVk5sU19SWEFER1ktM3IyWnRBYnJfUHpZdFpORGV0ZW5MX3ZR|5f2b956d32a0bbc71e157a4882a5f71a2911209857dcca482f5c09c3db1998e0"; tst=r; q_c1=a3f0f622e3be41268cbbe00b338591ab|1554621079000|1554621079000; __utmc=51854390; __utmz=51854390.1554621085.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20180522=1^3=entry_date=20180522=1; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c; __utma=51854390.1112982443.1554621085.1554621085.1554622229.2; __utmb=51854390.0.10.1554622229; __gads=ID=e43710b1b71ea145:T=1554630887:S=ALNI_Ma8l2AgdFiLWrAZZ8_8ovSLY6agQg',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}
r = requests.get('https://www.zhihu.com/', headers=headers)
print(r.text)
