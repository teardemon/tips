#!/usr/bin/env python
# encoding: utf-8

import hashlib


def hashing(filename):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(filename, 'rd') as bfile:
        buf = bfile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = bfile.read(BLOCKSIZE)
    return hasher.hexdigest()

if __name__ == '__main__':
    print hashing('/etc/shadow')
