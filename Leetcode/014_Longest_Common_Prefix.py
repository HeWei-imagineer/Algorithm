#又把下标当字符了，代码短，重写的时候发现的,下标混淆，混乱！！！
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] if len(strs)!=0 else ''
        for i in range(1,len(strs)):
            j = 0
            while j<len(prefix) and j<len(strs[i]):
                if strs[i][j] != prefix[j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix

s = Solution()
print(s.longestCommonPrefix(["aa","a"]))
