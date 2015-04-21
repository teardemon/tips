#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import string

def GenPassWord(length=10,chars=string.ascii_letters+string.digits):
    return ''.join([random.choice(chars) for i in range(length)])


if __name__ == "__main__":
    print GenPassWord()
