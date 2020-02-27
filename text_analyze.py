import jieba
jieba.add_word('叶文洁')
f=open('a.txt','r',encoding='utf-8')
txt=f.read()
f.close()
words=jieba.lcut(txt)
counts={}
for i in words:
    if len(i)==1:
        continue
    elif i=='一个':
        continue
    elif i=='没有':
        continue
    elif i in ['开始','还是','这是','进行','这些','发现','只有','东西','起来','一样','最后','可以','这种','只是','如果','出现','两个','这里','就是','这样','不是','那个','你们','他们','我们','这个','自己','现在','已经','可能','什么','看到','知道']:
        continue
    elif i in ['罗老师''罗博士','罗辑博士']:
        ii='罗辑'
    else:
        ii=i
    counts[ii]=counts.get(ii,0)+1
a=counts.items()
lst=list(a)
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    print('{0:^10}{1:>5}'.format(lst[i][0],lst[i][1]))
