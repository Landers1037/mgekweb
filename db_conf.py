
from pyquery import PyQuery as pq
from requests import get
from threading import Thread
import json

all = []
class my(Thread):
    def __init__(self,id,url):
        Thread.__init__(self)
        self.id = id
        self.url = url

    def run(self):
        get_ip(self.url)



def get_ip(url):
    data1 = []
    html = get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}).text
    ip = pq(html)("#ip_list tr td:nth-child(2)").items()
    port = pq(html)("#ip_list tr td:nth-child(3)").items()
    for i,p in zip(ip,port):
        data = {"ip":'',"port":""}
        data["ip"] = i.text()
        data["port"] = p.text()
        data1.append(data)

    all.append(data1)

    # return data1


my1 = my(1,'https://www.xicidaili.com/nn/')
my2 = my(2,'https://www.xicidaili.com/nt/')
my3 = my(3,'https://www.xicidaili.com/wn/')
my4 = my(4,'https://www.xicidaili.com/wt/')

my1.run()
my2.run()
my3.run()
my4.run()

with open('all.py','w',encoding='utf-8')as f:
    f.write('iplist = ')
    json.dump(all, f, indent=4, ensure_ascii=False)