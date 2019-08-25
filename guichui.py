import requests
from lxml import etree

url = 'https://www.luoxia.com/guichui/27426.htm'
while True:
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    html = requests.get(url, headers = headers)
    selector = etree.HTML(html.text)
    title = selector.xpath("//h1[@id='nr_title']/text()")[0]
    print(title)
    content = selector.xpath("string(//div[@id='nr1'])")
    # print(content)
    url = selector.xpath("//li[@class='next']/a/@href")[0]
    print(url)
    with open("鬼吹灯.txt", "a", encoding = 'utf-8') as f:
        f.write(title + '\n')
        f.write(content + '\n')
