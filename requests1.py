import requests
url='https://item.jd.com/100008348550.html'
try:
    r=requests.get(url)
    r.raise_for_status()
    print(r.encoding)
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
    print(r.apparent_encoding)
except:
    print('error')
