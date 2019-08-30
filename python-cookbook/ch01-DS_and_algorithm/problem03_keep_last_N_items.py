#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 10:22:59
# @Author  : zc12345 (18292885866@163.com)
# @Link    : https://github.com/zc12345/
# @Version : $Id$

from collections import deque

def search(lines, pattern, history=5):
	prev_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, prev_lines
		prev_lines.append(line)

if __name__ == '__main__':
	# generate test list
	l = []
	for i in range(10):
		tmp = 'python notebook, hello world'
		l.append(tmp)
	
	for line, prev_lines in search(l, 'python', 3):
		for pline in prev_lines:
			print(pline)
		print(line)
		print('-'*20)
	