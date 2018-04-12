class Solution:

    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        self.findNum(nums,target,4,ans)
        return ans


    def findNum(self,num,target,N,ans=[],temp=[]):
        if N==2:
            left,right = 0,len(num)-1
            while left<right:
                s = num[left] + num[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    ans.append(temp+[num[left],num[right]])
                    while left < right and num[left] == num[left+1]:
                        left += 1
                    while left < right and num[right] == num[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        elif N>2:
            i = 0
            while i<=len(num)-N:
                if i>0 and num[i]==num[i-1]:
                    i += 1
                    # it's continue,not break. baby~ 
                    continue
                self.findNum(num[i+1:],target-num[i],N-1,ans,temp+[num[i]])
                i += 1


if True:#__name__=='__main()__':
    s = Solution()
    ans = [] 
   
    print(s.fourSum([-1,0,1,2,-1,-4],-1))



