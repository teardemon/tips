#!/usr/bin/env python
# -*- coding: utf-8 -*-

fmt = '\033[0;3{}m{}\033[0m'.format  

class color:
    BLACK  = 0#黑
    RED    = 1#红
    GREEN  = 2#绿
    YELLOW = 3#棕
    BLUE   = 4#蓝
    PURPLE = 5#紫
    CYAN   = 6#青
    GRAY   = 7#灰


print fmt(color.BLACK  ,'kzc')
print fmt(color.RED    ,'kzc')
print fmt(color.GREEN  ,'kzc')
print fmt(color.YELLOW ,'kzc')
print fmt(color.BLUE   ,'kzc')
print fmt(color.PURPLE ,'kzc')
print fmt(color.CYAN   ,'kzc')
print fmt(color.GRAY   ,'kzc')

