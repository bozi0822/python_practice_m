# create by bob 2020-11-25

import requests
from lxml import etree

url = "https://www.tukuchina.cn/index.php?r=photo/channelInfo&chid=&q=%E5%B9%BF%E4%B8%9C"
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

response = requests.get(url=url, headers=headers)

text = response.text

html = etree.HTML(text, parser=etree.HTMLParser())

res = html.xpath("//div[contains(@class,'items')]/li/a/img/@data-original")
count = 1
for r in res:
    photoUrl = requests.get(r)
    with open(r"D:\PycharmProjects\demoProj\jpg" +'\\' + str(count) + ".jpg", 'wb+') as s:
        s.write(photoUrl.content)
    print(r + " " + "下载完成...")
    count += 1
