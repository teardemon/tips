#!/usr/bin/env python
#coding:utf-8
import string
import random
chars = string.ascii_letters + string.digits
def gen_passwd(length):
    password = ''.join(random.choice(chars) for x in range(length))
    return password
#password = ''.join(random.choice(chars) for x in range(random.randint(8,16)))
print gen_passwd(10)
