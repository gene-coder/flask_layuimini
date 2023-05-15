#!/usr/bin/env python
# -*- coding:utf-8 -*-
import configparser


# 定义读取文件
def readfile(filename, filetype):  
    content = ''
    if filetype == 'ini':
        content = configparser.ConfigParser()
        content.read(r'{}'.format(filename),encoding="utf-8")
    elif filetype == 'log':
        with open(r'{}'.format(filename), 'r', encoding='utf-8') as f:
            content = f.read()
    return content

# 写入文件,覆盖
def writefile(filename,filetype,content):
    if filetype == 'normal':
        with open(r'{}'.format(filename), 'w', encoding='utf-8',newline = None) as f:
            f.write(content)
    else:
        pass