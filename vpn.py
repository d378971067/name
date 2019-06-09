#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import os
import datetime
import hashlib


def liu(email, passwd):
        session_requests = requests.session()
        url = 'http://liu.gr/login'
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
                }
        start_html = session_requests.get(url, headers=headers)
        soup = BeautifulSoup(start_html.text, 'lxml')
        source = soup.find_all(attrs={"name": "_token"})
        token = source[0]['value']
        payload = {
                "email": email,
                "password": passwd,
                '_token': token
                }
        session_requests.post(url, data=payload, headers=headers)
        generalize_url = 'http://liu.gr/generalize'
        center_html = session_requests.get(generalize_url, headers=headers)
        center_soup = BeautifulSoup(center_html.text, 'lxml')
        center_source = center_soup.find_all(attrs={"name": "csrf-token"})
        headers = {
                'X-CSRF-TOKEN': center_source[0]['content']
                }
        sign_url = 'http://liu.gr/checkin'
        session_requests.post(sign_url, headers=headers)

liu('378971067@qq.com', '6533xd1007')

