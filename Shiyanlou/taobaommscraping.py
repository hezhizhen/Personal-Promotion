#!/usr/bin/env python3
# coding=utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os
import threading
import re

def main():
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    driver.get("https://mm.taobao.com/search_tstar_model.htm?")
    bs0bj=BeautifulSoup(driver.page_source,"lxml") # 解析HTML语言
    fp = open('mm.txt','r+')
    fp.write(driver.find_element_by_id('J_GirlsList').text)
    print("[*]OK GET MM's BOOK")
    MMsinfoUrl = bs0bj.findAll("a",{"href":re.compile("\/\/.*\.htm\?(userId=)\d*")})
    imagesUrl = bs0bj.findAll("img",{"data-ks-lazyload":re.compile(".*\.jpg")})
    items = fp.readlines()
    content1 = []
    n = 0
    m = 1
    while(n<14):
        content1.append([items[n].strip('\n'),items[m].strip('\n')])
        n += 3
        m += 3
    content2 = []
    for MMinfoUrl in MMsinfoUrl:
        content2.append(MMinfoUrl["href"])
    contents = [[a,b] for a,b in zip(content1, content2)]
    i = 0
    while(i<5):
        print("[*]MM's name:" + contents[i][0][0] + " with " + contents[i][0][1])
        print("[*]saving......" + contents[i][0][0] + "in the folder")
        perMMpageUrl = "http:" + contents[i][1]
        path = '/Users/hezhizhen/GitHub/Personal-Promotion/Shiyanlou/' + contents[i][0][0]
        mkdir(path)
        getperMMpageImg(perMMpageUrl, path)
        i += 1
    fp.flush()
    fp.close()
    number = 1
    for imageUrl in imagesUrl:
        url = "https:" + str(imageUrl["data-ks-lazyload"])
        html = urlopen(url)
        data = html.read()
        fileName = '/Users/hezhizhen/GitHub/Personal-Promotion/Shiyanlou/' + str(number) + '.jpg'
        fph = open(fileName,"wb")
        print("[+]Loading MM ...... "+fileName)
        fph.write(data)
        fph.flush()
        fph.close()
        number += 1
    driver.close()

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        print("[*]新建了名叫"+path+"的文件夹")
        os.makedirs(path)
    else:
        print("[+]名为"+path+"的文件夹已经创建成功")

def getperMMpageImg(MMURL, MMpath):
    owndriver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    owndriver.get(MMURL)
    print("[*]Opening......MM............")
    own0bj = BeautifulSoup(owndriver.page_source,"lxml")
    perMMimgs = own0bj.findAll("img",{"src":re.compile(".*\.jpg")})
    number = 2
    for perMMimg in perMMimgs:
        ImgPath = "https:"+str(perMMimg["src"])
        try:
            html = urlopen(ImgPath)
            data = html.read()
            fileName = MMpath+"/"+str(number)+'.jpg'
            fp = open(fileName,'wb')
            print("[+]Loading......her photo as"+fileName)
            fp.write(data)
            fp.close()
            fp.flush()
            number += 1
        except Exception:
            print("[!]Address Error!")

if __name__ == '__main__':
    main()
