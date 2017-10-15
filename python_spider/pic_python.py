import re
import requests
import urllib
from urllib import request

#home = 'http://search.dangdang.com/?key=Python&act=input'
#test.txt内容为home url的source view code
with open('test.txt','r', encoding='utf-8') as file:
    content = file.read()
file.close()
pic_url = re.findall("<img src='(.*?)' alt",content)
pic_url2 = re.findall("<img data-original='(.*?)' src",content)
pic_url.extend(pic_url2)#列表合并

tag = 0
for url in pic_url:
    print("Downloading---"+url)
    request.urlretrieve(url,'Pic%d.jpg'%tag)#从url下载图片
    tag = tag + 1
