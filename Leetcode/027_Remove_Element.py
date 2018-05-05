class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # if not nums:
        # 	return 0
        # left,right = 0,len(nums)-1
        # while left<right:
        # 	while left<right and nums[left]!=val:
        # 		left += 1
        # 	while left<right and nums[right]==val:
        # 		right -= 1
        # 	if left==right:
        # 		break
        # 	nums[left] = nums[right]
        # 	left += 1
        # 	right -= 1
        # return left+1 if left==right and nums[left]!=val else left

        #optimize
        left,right = 0,len(nums)
        while left<right:
        	if nums[left] == val:
        		nums[left] = nums[right-1]
        		right -= 1
        	else:
        		left += 1
        return right


if True:#__name__ == '__main()__':
	s = Solution()
	l = [4,5]
	print(s.removeElement(l,4))
	print(l)
