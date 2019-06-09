# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import os
from download import download
import requests
import datetime
import time
import chardet
import urllib
import sys

class main(download):
    def putname(self, name, sex, date):
        url = "http://www.xingyunba.com/quming/bzget.php"
        y = date[0:4]
        m = date[5:7]
        d = date[8:10]
        h = date[11:13]
        i = date[14:16]
        data = {
            'name': name,
            'sex': sex,
            'birth_address': '福建省-泉州市-丰泽区',
            'birth_date': date,
            'y': y,
            'm': m,
            'd': d,
            'h': h,
            'i': i,
            'zty': 1,
            'forMode': 1,
            'harea': 350503
        }
        html = requests.post(url, data)
        html.encoding = 'utf-8'
        text = html.text
        Soup = BeautifulSoup(text, 'lxml')
        Source = Soup.find_all("font", {'color': 'red'})[2]
        wuxing = Source.text[1]
        print wuxing

    def get_stroke(self,c):
        # 如果返回 0, 则也是在unicode中不存在kTotalStrokes字段
        strokes = []
        strokes_path="strokes.txt"
        with open(strokes_path, 'r') as fr:
            for line in fr:
                strokes.append(int(line.strip()))
        unicode_ = ord(c)

        if 13312 <= unicode_ <= 64045:
            return strokes[unicode_ - 13312]
        elif 131072 <= unicode_ <= 194998:
            return strokes[unicode_ - 80338]
        else:
            print("c should be a CJK char, or not have stroke in unihan data.")

    def get_wuge(self,name):
        name = name.decode('utf-8')
        length = len(name)
        tiange = self.get_stroke(name[0]) + 1
        renge = self.get_stroke(name[0]) + self.get_stroke(name[1])
        if length == 3:
            dige = self.get_stroke(name[1]) + self.get_stroke(name[2])
            zongge = self.get_stroke(name[0]) + self.get_stroke(name[1]) + self.get_stroke(name[2])
            waige = zongge - renge + 1
        else:
            dige = self.get_stroke(name[1]) + 1
            zongge = self.get_stroke(name[0]) + self.get_stroke(name[1])
            waige = zongge - renge + 2

        print tiange
        print renge
        print dige
        print zongge
        print waige

# print "请输入出生日期（例：2019/08/20 03:20）："
# birth_time = raw_input()
# print "请输入性别（1：男；2：女）："
# sex = raw_input()
name = raw_input("请输入姓：")
test = main()
# test.putname("戴", sex, birth_time)
# test.putname("戴", 1, '2019/08/20 03:20')
# test.get_stroke(name)
test.get_wuge(name)
