import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''


def fillList(lst,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            lst.append([tds[0].string,tds[1].string,tds[2].string])
            
def printList(lst,num):
    print('{0:^10}{1:{3}^20}{2:^10}'.format('top','名称','所在地',chr(12288)))
    for i in range(num):
        every=lst[i]
        print('{0:^10}{1:{3}^20}{2:^10}'.format(every[0],every[1],every[2],chr(12288)))
    
def main(num):
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    info=[]
    html=getHtmlText(url)
    fillList(info,html)
    printList(info,num)

main(78)
    
