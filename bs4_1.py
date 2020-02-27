import requests
from bs4 import BeautifulSoup
url='http://python123.io/ws/demo.html'
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
#print(soup.title)
#print(soup.html)
#print(soup.b)
#case1=soup.b
#print(soup.b.name)
#print(soup.b.attr)
#print(soup.a.attrs)
#print(soup.a.attrs['href'])
print(soup.body.prettify())
case2=soup.body.contents
for i in case2:
    print(i)
