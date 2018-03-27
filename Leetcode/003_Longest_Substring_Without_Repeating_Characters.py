#Longest Substring Without Repeating Characters
#it can find the specific substring
import math,logging
def lengthOfLongestSubstring(s):
	sum = set()
	count,head,k,index = 0,0,0,0
	while k<len(s) and index<len(s):
		k=index
		while k<len(s) and (s[k] not in sum):
			sum.add(s[k])
			k+=1
		sum = set()
		if count<k-index :
			count = k-index
			head = index
		index +=1
	return s[head:(head+count)]

#just find the length, using sliding window
#将出现过的字母用字典存起来，对应的值等于最新出现的字母的下标+1，下一次子串的头指针位置
def lengthOfLongestSubstring_1(s):
	mysum = set()
	mydic = {}
	i,count=0,0,0
	while(j<len(s)):
	for j,ch in enumerate(s):
		if ch not in mysum:
			mysum.add(ch)
			mydic[ch] = j+1
			count = max(count,j-i+1)
		else:
			i = max(mydic.get(ch),i)
			mydic[ch] = j+1
	return count

#test
logging.basicConfig(level=logging.INFO)
logging.info(lengthOfLongestSubstring_1('awsdasbrt'))




