class Solution:
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     nums.sort()
    #     length = i = 0
    #     while i<len(nums):
    #     	while i>0 and nums[i] == nums[i-1]:
    #     		i += 1
    #     		if i == len(nums):
    #     			return length
    #     	nums[length] = nums[i]
    #     	length += 1
    #     	i += 1
    #     return length
    #simplify
    def removeDuplicates(self, nums):
    	if not nums:
    		return 0
    	length = 0
    	for i in range(1,len(nums)):
    	 	if nums[i] != nums[length]:
    	 		length += 1
    	 		nums[length] = nums[i]
    	 	i += 1  
    	return length+1


if __name__ == '__main()__':
	s = Solution()
	l = [1,1]
	print(s.removeDuplicates(l))
	print(l)



