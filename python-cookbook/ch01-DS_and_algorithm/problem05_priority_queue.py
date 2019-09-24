#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-02 20:33:29
# @Author  : zc12345 (18292885866@163.com)
# @Link    : https://github.com/zc12345/
# @Version : $Id$

import heapq

class PriorityQueue:
    """docstring for PriorityQueue"""
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    """docstring for Item"""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'item ({!r})'.format(self.name)

def main():
    q = PriorityQueue()
    q.push(Item('fun'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('fork'), 1)
    print(q.pop())

    
if __name__ == '__main__':
    main()



