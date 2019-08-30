#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 10:14:46
# @Author  : zc12345 (18292885866@163.com)
# @Link    : https://github.com/zc12345/
# @Version : $Id$

def main():
	record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
	name, email , *others = record
	print(name, email, others)

	*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
	print(trailing, current)

	# unpack string
	line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
	uname, *fields, homedir, sh = line.split(":")
	print(uname, homedir, sh, fields)

	record = ('ACME', 50, 123.45, (12, 18, 2012))
	name, *_ , (day, *_) = record
	print(name, day)


if __name__ == '__main__':
	main()