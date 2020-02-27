import requests
url='https://www.amazon.cn/dp/B07K2VWX9S/ref=sr_1_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=27Z01EU6ROZVZ&keywords=ipad+pro&qid=1582294627&sprefix=ip%2Caps%2C170&sr=8-2'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
try:
    r=requests.get(url,headers=header)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('error')
    
