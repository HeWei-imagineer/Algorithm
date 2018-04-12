import math
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        k=math.inf
        for i in range(len(nums)-2):
        	l,r = i+1,len(nums)-1
        	if i>0 and nums[i]==nums[i-1]:
        		continue
        	while l<r:
        		s = nums[i] + nums[l] +nums[r]
        		if k > abs(target-s):
        			k = abs(target-s)
        			result = s
        		if s<target:
        			l += 1
        		elif s>target:
        			r -= 1
        		else:
        			l += 1
        			r -= 1
        			
        return result


if True: #__name__==:'__main()__':
	s = Solution()
	print(s.threeSumClosest([1,2,0],-100))