#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 10:08:02
# @Author  : zc12345 (18292885866@163.com)
# @Link    : https://github.com/zc12345/
# @Version : $Id$

import os

def main():
	data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
	name, shares, price, (year, mon, day) = data # unpack all data
	_, shares, price, _ = data # unpack part of data

	string = 'Hello'
	a, b, c, d, e = string # unpack string/ file object/ iterator/ generator
	print(a, b)

if __name__ == '__main__':
	main()
