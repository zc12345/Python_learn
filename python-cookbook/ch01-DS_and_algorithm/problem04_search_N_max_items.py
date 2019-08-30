#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 10:43:13
# @Author  : zc12345 (18292885866@163.com)
# @Link    : https://github.com/zc12345/
# @Version : $Id$

import heapq

def main():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # sort with keys
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}]
    print(heapq.nsmallest(3, portfolio, key=lambda s:s['price']))
    print(heapq.nlargest(3, portfolio, key=lambda s:s['price']))

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    nums_heap = list(nums)
    heapq.heapify(nums_heap)
    print(nums_heap)
    for i in range(len(nums)):
        print(heapq.heappop(nums_heap))

if __name__ == '__main__':
    main()