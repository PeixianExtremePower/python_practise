import requests
from bs4 import BeautifulSoup
import re

def getHtmlText(url,header):
    try:
        r=requests.get(url,headers=header)
        r.encoding=r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ''
    
def getList(url,lst):
    header={"user-agent":"Chrome/78.0.3904.108",'cookie':'SUB=_2AkMqIoz1f8PxqwJRmPAVxWPnaIpyyQnEieKcfn0uJRMyHRl-yD9kqnAdtRB6AaKiGlo5EMGmarV_R8Smhch43orNIups; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWJrDJ8H0hrSpRG9GpmEzGF; SINAGLOBAL=36.152.115.71_1568539588.125016; UOR=www.baidu.com,finance.sina.com.cn,; Apache=221.229.188.47_1582527598.608907; U_TRS1=0000002f.4f7fd0d5.5e53746e.3a240bc4; U_TRS2=0000002f.4f8ad0d5.5e53746e.b7778199; SR_SEL=1_511; lxlrttp=1578733570; ULV=1582527627518:2:2:2:221.229.188.47_1582527598.608907:1582527599273; FIN_ALL_VISITED=sz002291; FINA_V_S_2=sz002291'}
    for i in range(1,7):
        try:
            html=getHtmlText(url+str(i),header)
            soup=BeautifulSoup(html,'html.parser')
            trs=soup.find_all('tr')
            del trs[0]
            for tr in trs:
                try:
                    tds=tr.find_all('td')
                    lst.append([tds[0].string,tds[1].string])
                except:
                    continue
        except:
            continue
def getInfo(url,lst,file):
    header={"user-agent":"Chrome/78.0.3904.108",'cookie':'BAIDUID=966A18EB2B52EECA4DDD05DCF6C04242:FG=1; BIDUPSID=966A18EB2B52EECA4DDD05DCF6C04242; PSTM=1568030961; BDUSS=FdMSG5KUFg4T1dlbjFwNm1zYjFiWTJ2SGt4NTNybzhTMTdreFpuN2EtZWRFcWRkRVFBQUFBJCQAAAAAAAAAAAEAAAAgE15LNjRBQkM1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ2Ff12dhX9dV; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1447_21079_30790_30824_26350; delPer=0; BD_CK_SAM=1; PSINO=3; sugstore=0; COOKIE_SESSION=1476_0_7_5_4_5_0_0_5_3_0_2_29_0_0_0_1582527983_0_1582535627%7C9%230_0_1582535627%7C1; H_PS_645EC=4f86FPzWViy%2F0x1E05P%2BAlj5aCjS%2Fw%2Fs09zSqtSG964gMdaMLQbOEUFvX3A'}
    for i in range(len(lst)):
        try:
            html=getHtmlText(url+lst[i][0]+'股票',header)
            soup=BeautifulSoup(html,'html.parser')
            names=soup.find_all(attrs={'class':'op-stockdynamic-moretab-info-name'})
            values=soup.find_all(attrs={'class':'op-stockdynamic-moretab-info-value'})
            for j in range(len(names)):
                try:
                    lst[i].append(names[j].string)
                    lst[i].append(values[j].string)
                except:
                    continue
        except:
            continue
        '''lis=soup.find_all('li')
        for li in lis:
            if li.span.string in ['今开','昨收','最高','最低','换手率','成交量','市盈率','总市值']:
                #span=li.find('span',attrs={'class':'op-stockdynamic-moretab-info-name'})
                lst[i].append(li.span.string)
                span_2=li.find(attrs={'class':'op-stockdynamic-moretab-info-value'})
                lst[i].append(span_2.string)
            else:
                continue'''
    f=open(file,'w',encoding='utf-8')
    for every in lst:
        f.write(','.join(every)+'\n')
    f.close()




def main():
    ListUrl='http://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/ggtj/index.phtml?p='
    InfoUrl='https://www.baidu.com/s?wd='
    List=[]
    file='Infomation_version2.csv'
    getList(ListUrl,List)
    getInfo(InfoUrl,List,file)

main()
