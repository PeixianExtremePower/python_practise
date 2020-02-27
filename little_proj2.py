import requests
import re

def getHtmlText(url):
    try:
        header={"user-agent":"Chrome/78.0.3904.108","Cookie":'miid=1466173064755755224; cna=ai79Fd981QsCASSYc3UlLItx; thw=cn; v=0; cookie2=1bb6743291ed588b6f24b0925a5aab5a; t=402bd4bc0994855a995ecd5e301e1313; _tb_token_=e9e75b5d73361; _samesite_flag_=true; tfstk=cIuOBAis4pvgurGXVBxnGrN4qTCAaCbTH1wPkIFQWyRCH9QAlsA-r4n7qhNRBydd.; sgcookie=DzBsx%2FrkqeUxIPu1mdBUh; uc3=vt3=F8dBxd3xJW9dJ8iQSXU%3D&nk2=0rzKWzKzoKFVWMRBIP5NKQ%3D%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUBQarR8H5CMMg%3D%3D; csg=1ad884bc; lgc=%5Cu51B0%5Cu4E0E%5Cu706B%5Cu4E4B%5Cu6B4C370826; dnk=%5Cu51B0%5Cu4E0E%5Cu706B%5Cu4E4B%5Cu6B4C370826; skt=e8a88ead46d29900; existShop=MTU4MjQ0Njk5Mw%3D%3D; uc4=id4=0%40U2LC4M2ZRuJ8Ne7ukClaDuqyxK08&nk4=0%400A3VUVThZCfHCYg41TCpWiiMj7sHBVdEi7Ay; tracknick=%5Cu51B0%5Cu4E0E%5Cu706B%5Cu4E4B%5Cu6B4C370826; _cc_=URm48syIZQ%3D%3D; tg=0; mt=ci=99_1; enc=KYkaqxPE1RrgDe97eMp3vk4ifxcygIOFWw8P2Qc0dfrc%2BEAaem6PsRJGlXLIXZhNUld7AZyDKonq8aGOg2XDvg%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTUOLcdMcmD5A%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=V32FPkk%2FgihF%2FS5nr3O5&tag=8&cookie15=VT5L2FSpMGV7TQ%3D%3D&pas=0; JSESSIONID=809697C5D0063158974EE7E567B14DBC; l=cBPVdwJHqwknIT3yBOfaourza779uIRb4sPzaNbMiICP9L1H5JgVWZ2qNnTMCnGVp6tvJ3Jt3efYBeYBqsqBfdW22j-la; isg=BEFBvrrg-8IY_hTSUyuuj4kxUI1bbrVgeiiFG6OWqMinimFc6r6zMG3IaP7Mgk2Y'}
        r=requests.get(url,timeout=30,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def fillList(info,html):
    try:
        GoodsNames=re.findall(r'\"raw_title\"\:\".*?\"',html)
        GoodsPrices=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        for i in range(len(GoodsNames)):
            try:
                GoodsName=eval(GoodsNames[i].split(':')[1])
                GoodsPrice=eval(GoodsPrices[i].split(':')[1])
                info.append([GoodsName,GoodsPrice])
            except:
                continue
    except:
        print('')
    

def printList(info):
    #print('{0:^4}{1:<10}{2:>10}'.format('number','GoodsName','GoodsPrice'))
    #counts=1
    f=open('Goods_info_2.csv','w',encoding='utf-8')
    for every in info:
        #print('{0:^4}{1:<10}{2:>10}'.format(counts,every[0],every[1]))
        #counts+=1
        f.write(','.join(every)+'\n')
    f.close()
        

def main():
    goods=input('please input goods:')
    num=eval(input('please pages that u want to look:'))
    start_url='https://s.taobao.com/search?q=' + goods
    info=[]
    for i in range(num):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHtmlText(url)
            fillList(info,html)
        except:
            continue
    printList(info)

main()            
            
            
