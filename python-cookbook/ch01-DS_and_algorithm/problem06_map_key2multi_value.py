#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-03 00:20:54
# @Author  : zc12345 (18292885866@163.com)
# @Link    : https://github.com/zc12345/
# @Version : $Id$

from collections import defaultdict

def main():
    d = {
    'a': [1, 2, 3],
    'b': [4, 5]
    }
    print(d)

    e = defaultdict(list)
    e['a'].append(1)
    e['a'].append(2)
    e['a'].append(1)
    print(e)

    f = defaultdict(set)
    f['a'].add(1)
    f['a'].add(2)
    f['a'].add(2)
    print(f)

    pairs = [[0,0],[0,0]]
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)

    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)

if __name__ == '__main__':
    main()
