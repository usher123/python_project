import urllib
import re
import os
import sys
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.flag = 0
            self.links = []
            self.title=""
            self.other = []
        def handle_starttag(self, tag, attrs):
            if tag =="meta" and "charset" in attrs:
               print("1")
                
            if tag == "a"  :
                if len(attrs) == 0: pass
                else:
                    for (variable, value)  in attrs:
                        if variable == "href":
                            self.links.append(value)

            if tag =="href":
                self.flag=1
            if tag == "img":
                for (name,value) in attrs:
                    if name =='src':
                        self.other.append(value)

        def handle_data(self,data):
            if self.flag == 1 and len(self.href)==0:
                self.href=data
                self.flag==0

def save_htmlpage(url):
    print(url)
    ds = open ('grap2.txt','wb')
    try:
        ds.write(urllib.urlopen(url).read().decode('utf-8'))
        ds.close()
    except UnicodeDecodeError:
        print('decode error')

    file = open ('grap2.txt','r')
    data = file.read()
    bs.write(data)
    

def __int__():
    reload(sys)
    sys.setdefaultencoding("utf8")

def save_link(url,g):
    try:
        data = urllib.urlopen(url).read().decode('utf-8')
    except UnicodeDecodeError:
        print("link erro")
        return
    wp = MyHTMLParser()
    wp.feed(data)
    ws = open('href_links.txt','a')
    gs = open('image_links.txt','a')
    for link in wp.links:
        ws.write(link +"\n") 
    if g ==1:
        ws.write('tag'+'\n')
        g =0
    for imag in wp.other:
        gs.write(imag +'\n')


def true_link(link):
    if "http:" in link:
        return 1!=2
    else:
        return 1==2
    html = urllib.urlopen(link).getcode()
    if html ==200:
        return True
    else:
        return False


if __name__ == "__main__":
    __int__()
    g = 1
    bs = open('grap.txt','a')
    file = open('href_links.txt','r')
    a = "http://www.baidu.com"
    save_htmlpage(a)
    save_link(a,g)
    l = 'y'
    while l != 'n':
        n=1
        while n != 0:
            link = file.readline()
            if true_link(link) == True:
                n = 0
            if link == "tag":
                l =input('this is tagbull,do you want to go on:\'y\' or\'n\'' )
                if l == 'y':
                    n = 1
                    incm = open('href_links.txt','a')
                    incm.write('tag'+'/\n')
                    incm.close()
                if l == 'n':
                    pass
        save_htmlpage(link)
        save_link(link,g)
    bs.close()
    w = input('do you want to delete data?:\'y\' or \'n\'')
    if w == 'y':
        os.system('rm grap.txt href_links.txt')

    
        

