#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

SWITCH_URL = "http://10.32.64.64:8000/info/switch/"
SERVER_URL = "http://10.32.64.64:8000/info/server/"

def get_content(SERVER_URL):
    """从指定url获取数据"""
    content = requests.get(SERVER_URL).content
    return content


def filter_host(hosts,*key_words):
    '''根据关键字过滤主机'''
    result=[]
    for host in hosts:
        for i in key_words:
            if i in host:
                result.append(host)
                break
    return result


def vfilter_host(hosts,*key_words):
    '''根据关键字过滤主机'''
    results=[]
    for host in hosts:
        for i in key_words:
            if i in host:
                host=None
            if host is None:
                break
        if host is not None:
            results.append(host)
    return results

def get_windows():
    hosts = get_content(SERVER_URL).split('\n')
    filters = ["windows"]
    vfilters = ["退役", "内部机房", "VC"]
    hosts = filter_host(hosts, *filters)
    hosts = vfilter_host(hosts, *vfilters)
    windows = []
    for i in hosts:
        i = i.split(',')
        if i[1] != '':
            windows.append(i[1])
        elif i[2] != '':
            windows.append(i[2])
        elif i[3] != '':
            windows.append(i[3])
    return  windows


def get_linux():
    hosts = get_content(SERVER_URL).split('\n')
    filters = ["linux"]
    hosts = filter_host(hosts, *filters)
    linuxs = []
    for i in hosts:
        i = i.split(',')
        if i[1] != '':
            linuxs.append(i[1])
        elif i[2] != '':
            linuxs.append(i[2])
        elif i[3] != '':
            linuxs.append(i[3])
    return linuxs

if __name__ == '__main__':
    print get_linux()

