#!/usr/bin/env python

import sys
input= sys.stdin.readline

vol = {'a','e','i','o','u'}
while True:
	test = input().rstrip()
	if test == 'end':
		break

	v_flag = 0 
	v_cnt = 0
	c_cnt = 0
	err = 0  
	for i in range(len(test)):
		if i > 0:
			if test[i] == test[i-1]:
				if test[i] != 'e' and test[i] != 'o':
					err = 1
					break
		if test[i] in vol:
			v_flag = 1
			v_cnt += 1
			c_cnt = 0
			if v_cnt == 3:
				err = 1
				break
		else:
			v_cnt = 0
			c_cnt += 1
			if c_cnt == 3:
				err = 1
				break

	if (err != 1) and (v_flag == 1):
		print("<"+ test +"> is acceptable.")
	else:
		print("<" + test + "> is not acceptable.")
