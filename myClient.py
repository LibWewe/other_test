#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: myClient.py
# @Time: 2018/2/8 12:14
# @Last Modified time: 2018/2/8 12:14
# @Explain: This file is for ...



import  socket
import  datetime

HOST = input("IP:")
PORT = eval(input("PORT:"))

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((HOST,PORT))

while True:
    user_input=input("msg:").strip()
    s.send(user_input.encode())
    data=s.recv(1024)
    cur_time=datetime.datetime.now().strftime("%X")
    if data=="quit":
        break
    print("[%s]recv:"%cur_time,data)

s.close()








