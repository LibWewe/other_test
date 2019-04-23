#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Filename: tcp_http.py
@version: v1.0 
@author: WeWe
@Time: 2018/3/8 20:23
@Last Modified time: 2018/3/8 20:23
@Explain: This file is for ...
'''

import socket





sockstr = '''
GET https://www.baidu.com/ HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Accept-Language: zh-CN,zh;q=0.8
'''
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.baidu.com', 80))
    print("connect......")
    s.send(sockstr.encode("utf-8"))
    print("send..........")
    buf = s.recv(1024)
    print("recv...........")
    while len(buf):
        print(buf.decode("gbk"))
        buf = s.recv(1024)