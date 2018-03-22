# #Longest Palindromic Substring

# #判断每一个位置是否是中心点，以及和它后一个点组合是否是中心点

# class Solution:
#     def longestPalindrome(self, s):
#         for i in range(len(s)):
#         	k1,k2,count = 0,0,0
#         	record = []
#         	while i<len(s):
#         		k1=k2=i
#         		#the length of palindrome is odd
# 			    while (s[k1]==s[k2] and k1>=0 and k2<len(s)):
# 					k1-=1
# 					k2+=1
# 				#the length of palindrome is even
# 			    if s[i]==s[i+1]:
# 					k1,k2=i,i+1
# 					while s[k1]==s[k2] and k1>=0 and k2<len(s):
# 						k1-=1
#  						k2+=1
# 				if count < k2-k1-2:
# 					count = k2-k1-2
# 					record.append(k1+1)
#  					record.append(k2)
# 				i += 1
#         return s[record[0],record[1]]

# s = Solution()
# s.longestPalindrome('abcdcbe')

import itertools

# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     OddList = itertools.takewhile(lambda x: x<=2*N,itertools.count(1,2))
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     ns = itertools.cycle([1,-1])
#     # step 4: 求和:
#     return sum(map(lambda x : next(ns)*4/x,OddList))

# # 测试:
# print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert 3.1414 < pi(10000) < 3.1415
# print('ok')

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)