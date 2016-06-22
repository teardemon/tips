#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Queue
import nmap
import urllib
from multiprocessing.dummy import Pool as ThreadPool
import requests
from hosts import get_windows


sport = '21,23,135,139,445,593,873,1433,3306,3389'
hosts = get_windows()
q = Queue.Queue()


def check_ports(ip):
    nm = ''
    try:
        nm = nmap.PortScanner()
    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(0)
    try:
        nm.scan(hosts=ip, arguments=' -v -Pn -sS -p ' + sport)
    except Exception, e:
        print "Scan erro:", e
    for host in nm.all_hosts():
        for proto in nm[ip].all_protocols():
            lport = nm[ip][proto].keys()
            lport.sort()
            for port in lport:
                state = nm[host][proto][port]['state']
                if state == 'open':
                    q.put((ip, str(port), nm[host][proto][port]['state']))


def sendImMsg(msg, imlist, level=10):
    msg = urllib.quote(msg)
    url = "http://10.32.64.64:8000/sendmsg/?accounts=%s&content=%s\
        &level=%s" % (imlist, msg, level)
    print url
    urllib.urlopen(url)

if __name__ == "__main__":
    pool = ThreadPool(20)
    results = pool.map(check_ports, hosts)
    pool.close()
    pool.join()
    echo = []
    echo.append("Windows服务器端口扫描，下列端口公网可访问请及时更新防火墙配置")
    ip_port = {}
    while not q.empty():
        info = q.get()
        ip = info[0]
        port = info[1]
        if ip_port.has_key(ip):
            ip_port[ip] = ip_port[ip] + ',' + port
        else:
            ip_port[ip] = port

    print ip_port
    hosts = get_content().split('\n')
    for ip in ip_port:
        hostinfo = filter_host(hosts, str(ip) + ',')
        hostinfo = hostinfo[0].split(',')
        echo.append(ip+'\t'+ip_port[ip]+'\t'+hostinfo[9]+'\t'+hostinfo[10]+'\t'+hostinfo[11])
    imlist = '8838'
    if len(echo) > 1:
        msg = '\n'.join(echo)
        sendImMsg(msg, imlist)
