import base64
from requests import get
import random

url = ['https://heikejilaila.xyz/keji.php?id=22c7b9fdda20bb7405b270cd75971f66',
       'https://raw.githubusercontent.com/eycorsican/rule-sets/master/kitsunebi_sub',
       'https://raw.githubusercontent.com/ssrsub/ssr/master/ssrsub',
       'https://youlianboshi.netlify.com/',
       'http://v2ray.qlolp.ml'
       ]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.80 Safari/537.36'}
def xhj():
    geturl = random.choice(url)
    try:
        html = get(geturl,headers=headers).text
        lists = base64.urlsafe_b64decode(html).decode('utf-8')
        lists = lists.split('\n')
        datajson = {"lists": lists}
    except:
        datajson = {"lists": ['null','null','null']}

    return datajson
