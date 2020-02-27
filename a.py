import jieba
import wordcloud

f=open('7.txt','r',encoding='utf-8').read()
jieba.add_word('伏地魔')
words=jieba.lcut(f)
txt=' '.join(words)
w=wordcloud.WordCloud(font_path='msyh.ttc',\
                      width=1000,height=700,background_color='white',\
                      )
w.generate(txt)
w.to_file('77.png')
                      
