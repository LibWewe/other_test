#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: myServerSocket.py
# @Time: 2018/2/8 11:11
# @Last Modified time: 2018/2/8 11:11
# @Explain: This file is for ...


import socketserver
import datetime

class MySocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("有一个新连接：",self.client_address)
        while True:
            data=self.request.recv(1024)
            if not data:
                break
            nowtime=datetime.datetime.now().strftime("%X") #获取当前的时间
            print("[%s]recv:"%nowtime,data)
            self.request.send(data.upper())

if __name__ == "__main__":
    HOST="192.168.43.23"
    PORT=50007
    s=socketserver.ThreadingTCPServer((HOST,PORT),MySocketServer)
    print("listen....")
    s.serve_forever()










