import requests
from lxml import etree
import urllib.parse
import threading

def thredingFunc(urlRoot):
    url = urllib.parse.urljoin("https://www.yangguiweihuo.com/8/8257/", urlRoot)
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    html = requests.get(url, headers = headers)
    selector = etree.HTML(html.text)
    title = selector.xpath("//h1/text()")[0]
    print(title)
    contentList = selector.xpath("//div[@id='content']/text()")
    content = '\n'.join((''.join(contentList)).split())
    with open((title + ".txt").replace('?？', ''), "a") as f:
        f.write('\n' + title + '\n')
        f.write(content)

url = "https://www.yangguiweihuo.com/8/8257/"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
html = requests.get(url, headers = headers)
selector = etree.HTML(html.text)
List = selector.xpath("//div[@class='listmain']/dl/dd/a/@href")
List2 = list(set(List))

thread = []
for each in List2:
    thread.append(threading.Thread(target = thredingFunc, args = (each,)))

for t in thread:
    t.start()

for t in thread:
    t.join()