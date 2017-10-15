'''
ip被封禁了，不折腾了，回来再搞
'''
import requests
from bs4 import BeautifulSoup
#import pandas as pd
import random
import time
import re

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN, zh; q=0.8',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
}
proxies_list = [
    '182.88.134.35:8123',
    '210.22.159.83:8080'
]
proxies = {
    'https':'http://{}'.format(random.choice(proxies_list))
}
home = 'https://movie.douban.com/chart'
#home = 'https://www.bilibili.com/video/online.html'
#try:
res = requests.get(home, headers = headers, proxies = proxies).text
soup = BeautifulSoup(res, 'html.parser')
type_id = re.findall('type=(.*?)&amp', str(soup.findAll('div',{'class':'types'})[0]))
print(type_id)
#except requests.exceptions.ConnectionError:
#    print("!!!connect refused")

'''
urls = []
limits = []
#
for num in type_id:
    for i in range(100,-10,-10):
        limits_url = 'https://movie.douban.com/j/chart/top_list_count?type='+num+'&interval_id='+str(i)+'%3A'+str(i-10)
        limits_res = requests.get(limits_url, headers = headers).text
        limits.append(re.findall('"total":"(.*?)"', limits_res))

        time.sleep(3)
#
time.sleep(3)
print(type_id)
for num in type_id:
    limits_url = 'https://movie.douban.com/j/chart/top_list_count?type='+num+'&interval_id=100%3A90'
    limits_res = requests.get(limits_url, headers = headers).text
    limits.append(re.findall('"total":"(.*?)"', limits_res))
    time.sleep(3)

print(limits)
'''