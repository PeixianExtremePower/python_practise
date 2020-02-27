import getHtmlText
import fillList
import printList

url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
info=[]
html=getHtmlText.getHtmlText(url)
fillList.fillList(info,html)
printList.printList(info)

