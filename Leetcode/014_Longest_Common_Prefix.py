class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] if len(strs)!=0 else ''
        for i in range(1,len(strs)):
        	for j,ch in enumerate(i):
        		if  ch != prefix[i]:
        			prefix = prefix[:i]
        			break
        return prefix