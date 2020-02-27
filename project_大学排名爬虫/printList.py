def printList(lst):
    f=open('list.txt','w',encoding='utf-8')
    #print('{0:^10}{1:{3}^20}{2:^10}'.format('top','名称','所在地',chr(12288)))
    #for i in range(len(lst)):
    #        every=lst[i]
    #        print('{0:^10}{1:{3}^20}{2:^10}'.format(every[0],every[1],every[2],chr(12288)))
    for line in lst:
        f.write(line[0]+'\t'+line[1]+'\n')
    f.close
