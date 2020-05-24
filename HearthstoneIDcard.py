import requests
from lxml import etree
import pickle
dict_1 = {}
num = 0
filename = 'd\\hearthstone.pkl'#存储路径，自己填
#爬取字典 因为11000的时候网页已经没有词条了，所以这里num是11000
while(num<=11000):
    url = 'https://hearthstone.huijiwiki.com/index.php?title=%E5%B1%9E%E6%80%A7:'+'CardId&limit=500&offset=%d&value=&from=&until='%num
    r = requests.get(url)
    r_xpath = etree.HTML(r.text)
    r_x = r_xpath.xpath('//tr/td[1]/a/text()')
    r_x1 = r_xpath.xpath('//tr/td[2]/text()')
    for i in range(0,len(r_x)-1):
        dict_1[r_x[i]]= r_x1[i]
        print(dict_1[r_x[i]])
    num +=500
f = open('filename','wb')
pickle.dump(dict_1,f)
f.close()
'''
#读取字典
f = open('filename','rb')
r = pickle.load(f)
f.close()
'''
