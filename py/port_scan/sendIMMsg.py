#!/usr/bin/env python
# encoding: utf-8


import urllib


def sendImMsg(msg, imlist, level=10):
    msg = urllib.quote(msg)
    url = "http://10.32.64.64:8000/sendmsg/?accounts=%s&content=%s" % \
        (imlist, msg)
    urllib.urlopen(url)

if __name__ == '__main__':
    msg = 'test'
    imlist = '8838'
    sendImMsg(msg, imlist)
