#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 9:05
# @Author  : Shao
# @File    : requests_1.py
# @Desc    :


import requests
import json


# 输入测试网站，返回结果json串
class tLogin:  # 注意若类名中出现test则pycharm会识别为在执行单元测试
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def get_back(self):
        r = requests.post(self.url, headers=self.headers, data=self.data)
        return r.json()


# 读取本地json文件，返回一个账号密码组合列表
class readFile:
    def __init__(self, f_path):
        self.__f_path = f_path

    def read_file(self):
        with open(self.__f_path, "r", encoding='utf-8') as f:
            f_list = json.load(f)
            f_key = list(f_list.keys())
            f_vlaues = f_list[f_key[0]]  # 第一组
            data = []  # 存储账号名和密码的组合
            for i in f_vlaues:
                for j in f_vlaues:
                    data_item = {
                        "username": i,
                        "password": j
                    }
                    data.append(data_item)
        return data


# 将返回json保存为文件
class saveFile:
    pass


if __name__ == '__main__':
    url = "http://localhost:3000/login/loginSub"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://localhost:3000/"
    }
    f = readFile("D:/projects/python36/learn/1.json")
    data = f.read_file()  # data为账号密码的组合
    for i in data:
        try:
            test_login = tLogin(url, headers, i)
            t_req = test_login.get_back()
            if t_req["code"] == "200":
                j = dict(t_req, **i)
                print(j)
            else:
                j = dict(t_req, **i)
                print(j)
        except:
            print("链接有问题！")
