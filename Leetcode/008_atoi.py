#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
class Solution:
    def myAtoi(self, str):
    	str = str.strip(' ')
    	s = ''
    	if len(str):
    		if str[0]=='-':
    			sign = -1
    		elif str[0]=='+':
    			sign = 1
    		else:
    			sign = 0

    		for i in range(abs(sign),len(str)):
    			if str[i] >= '0' and str[i] <= '9':
    				s = s + str[i]
    			else:
    				break

    		if len(s):
    			result = int(s) if sign != -1 else int(s)*sign
    			if result<-2147483648:
    				return -2147483648
    			elif result>2147483647:
    				return 2147483647
    			else:
    				return result
    	return 0

s = Solution()
print(s.myAtoi("1"))


