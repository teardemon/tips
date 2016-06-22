#!/usr/bin/env python
# encoding: utf-8

import sys
import nmap
import Queue
from multiprocessing.dummy import Pool as ThreadPool

q = Queue.Queue()
result = Queue.Queue()

tnets=['192.168.127.0/24', '192.168.167.0/24', '10.16.64.0/23',
       '192.168.180.0/22', '10.17.64.0/23', '192.168.184.0/22',
       '10.18.64.0/23', '192.168.106.0/24', '192.168.112.0/23',
       '192.168.111.0/24']


def check_alive(net):
    try:
        nm = nmap.PortScanner()
    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)
    try:
        nm.scan(hosts=net, arguments='-v -sn')
    except Exception, e:
        print "Scan error:" + str(e)
    print 'check ' + net
    print '-------------'
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print host
    print '-------------'

if __name__ == '__main__':
    for net in tnets:
        check_alive(net)
