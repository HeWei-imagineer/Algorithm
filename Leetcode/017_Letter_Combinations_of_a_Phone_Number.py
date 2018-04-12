class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits)==0:
        	return []
        elif len(digits)==1:
        	return [s for s in mapping[digits[0]]]
        else:
        	pre = self.letterCombinations(digits[:-1])
        	addition = mapping[digits[-1]]
        	return [s+c for s in pre for c in addition]


if True: #__name__==:'__main()__':
	s = Solution()
	print(s.letterCombinations('23'))