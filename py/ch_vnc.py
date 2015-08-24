#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
'''
output file:

'''

logname = 'C:\\Program Files\\RealVNC\\VNC Server\\Logs\\vncserver.log'
result_log = 'vnc_result.log'

f_disconn = re.compile(r'Connections: disconnected: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}.*\(\[AuthFailure\]')
#客户端认证失败，未登陆
s_conn = re.compile(r'Connections: authenticated: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}')
#客户端认证成功，与VNC server建立连接

#下列五种匹配均为客户端建立连接之后断开
server_disconn = re.compile(r'Connections: disconnected: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}.*\(\[SessionClosed')
s_disconn = re.compile(r'Connections: disconnected: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}.*\(\[ViewerClosed')
t_disconn = re.compile(r'Connections: disconnected: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}.*\(\[IdleTimeout')
e_disconn = re.compile(r'Connections: disconnected: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}.*\(\[EndOfStream')
g_disconn = re.compile(r'Connections: disconnected: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}::[0-9]{4,5}.*\(\[System\] read')


def get_auth_lines():
    templ=[]
    try:
        logfile = open(logname,'r')
        for i in logfile.readlines():
            if re.search(s_conn,i) or re.search(server_disconn,i) or re.search(s_disconn,i) \
               or re.search(f_disconn,i) or re.search(t_disconn,i) or re.search(e_disconn,i)\
               or re.search(g_disconn,i):
                templ.append(i)
    except IOError as err:
        print 'File error:',err
    return templ

def get_log_report():
    templ =get_auth_lines()
    outcontent = []
    paired = []
    for i in range(len(templ)):
        if re.search(f_disconn,templ[i]):
            t1 = templ[i].split()
            l = '\t'.join([t1[1],t1[6],' '.join(t1[7:])])+'\n'
            outcontent.append(l)
        elif re.search(s_conn,templ[i]):
            t2 = templ[i].split()
            t2[6] = t2[6].rstrip(',')
            c_pair = False
            for j in range(i+1,len(templ)):
                if t2[6] in templ[j]:
                    c_pair = True
                    t3 = templ[j].split()
                    l = '\t'.join([t2[1],t2[6],t2[8],t3[1]])+'\n'
                    paired.append((t3[1],t3[6]))
                    outcontent.append(l)
                    break
            if c_pair == False:
                l = '\t'.join([t2[1],t2[6],' '.join(t2[7:])])+'\n'
                outcontent.append(l)

        else:
            t4 = templ[i].split()
            if ((t4[1],t4[6])) in paired:
                continue
            else:
                l = '\t'.join([t4[1],t4[6],' '.join(t4[7:])])+'\n'
                outcontent.append(l)
    return outcontent


if __name__ == '__main__':
    outcontent = get_log_report()
    with open(result_log,'w') as outfile:
        outfile.writelines(outcontent)
