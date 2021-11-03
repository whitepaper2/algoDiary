#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 下午4:46
# @Author  : pengyuan.li
# @Site    : 
# @File    : 01requests.py
# @Software: PyCharm
import urllib.request
from urllib import request, parse
from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.request import URLError
from urllib.request import ProxyHandler


def myUrlopen():
    res = urllib.request.urlopen("https://python.org")
    print(type(res))
    # class http.client.Response
    print(res.read().decode('utf-8'))
    print(res.getcode())
    print(res.getheaders())


def myRequest():
    url = "http://httpbin.org/post"
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        'Host': "httpbin.org"}
    inputForm = {'name': "Germany"}
    data = bytes(parse.urlencode(inputForm), encoding='utf-8')
    req = request.Request(url=url, data=data, headers=headers, method="POST")
    res = request.urlopen(req)
    print(res.read().decode('utf-8'))


def myAuth():
    """
    @todo:执行报错？？？
    :return:
    """
    username = "username"
    password = "password"
    url = "http://localhost:5000"
    p = HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    auth_handler = HTTPBasicAuthHandler(p)
    opener = build_opener(auth_handler)
    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        print(html)
    except URLError as e:
        print(e.reason)


def myProxy():
    """
    @todo:执行报错？？？
    :return:
    """
    proxy_handler = ProxyHandler({'http': 'http://127.0.0.1.8080', 'https': "https://127.0.0.1.9743"})
    opener = build_opener(proxy_handler)
    try:
        response = opener.open("https://www.baidu.com")
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def myCookies():
    pass


if __name__ == "__main__":
    # myRequest()
    # myAuth()
    myProxy()
