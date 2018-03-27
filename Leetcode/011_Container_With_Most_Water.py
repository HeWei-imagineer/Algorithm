class Solution:
    def maxArea(self, height):
    	"""
        :type height: List[int]
        :rtype: int
        """
    	star,end,area=0,len(height)-1,0
    	while star<end:
        	h = min(height[star],height[end])
        	area = max(area,(end-atar)*h)
        	while star<end:
        		if height[star] > height[end]:
        			end -= 1
        		else:
        			star += 1
        		if max(height[star],height[end])>h:
        			break
    	return area		

