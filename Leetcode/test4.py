# # Median of Two Sorted Arrays  
# # class Solution:
# #     def findMedianSortedArrays(self, nums1, nums2):
# #         """
# #         :type nums1: List[int]
# #         :type nums2: List[int]
# #         :rtype: float
# #         """
# #         sum,k1,k2 = [],0,0
# #         while k1<len(nums1) and k2<len(nums2):
# #             if nums1[k1]<=nums2[k2]:
# #                 sum.append(nums1[k1])
# #                 k1+=1
# #             else:
# #                 sum.append(nums2[k2])
# #                 k2+=1
# #         if k1==len(nums1):
# #             for i in range(k2,len(nums2)):
# #                 sum.append(nums2[i])
# #         if k2==len(nums2):
# #             for i in range(k1,len(nums1)):
# #                 sum.append(nums1[i])
# #         print(sum)
# #         if len(sum)%2:
# #             return int(sum[len(sum)//2])
# #         else:
# #             return int((sum[len(sum)//2]+sum[len(sum)//2-1])/2)
# #  #test
# # nums1 = [1,3]
# # nums2 = [2,4]            
# # s = Solution()
# # a = s.findMedianSortedArrays(nums1, nums2)   
# # print(a) 


# #There is another simple way to solute the proplem. It's clever
# #cut A(m) into two part(i,m-i),left_part_A < right_part_A,and do the same thing to B(n,finally we can get left_part_A and left_part_B < right_part_A and right_part_B
# #so just need find i, A[i]>=B[j-1],A[i-1]<=B[j],j=(m+n+1)/2-i  then consider the edge values

# #自己易忽略的点，j>0，j=(m+n+1)/2-i,所以n>m，

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         A,B,m,n = nums1,nums2,len(nums1),len(nums2)
#         if m>m:
#              A,B,m,n = nums2,nums1,len(nums2),len(nums1)
#         imin,imax = 0,m
#         while imin < imax : 
#             i = (imin + imax)//2
#             j = (m+n+1)//2-i
#             if i>0 and A[i-1]>B[j]:
#                 imax = i-1
#             elif i<m and A[i]<B[j-1]:
#                 imin = i+1
#             else:
                
#                 if i==0: max_of_left = B[j-1]
#                 elif j==0: max_of_left = A[i-1]
#                 else: max_of_left = max(B[j-1],A[i-1])

#                 if (m+n)%2==0:
#                     return max_of_left

#                 if i==m: min_of_right = B[j]
#                 elif j==n: min_of_right = A[i]
#                 else: min_of_right = min(B[j],A[i])

#                 return (max_of_left+min_of_right)/2
                

# nums1 = [1,3]
# nums2 = [2,4]            
# s = Solution()
# a = s.findMedianSortedArrays(nums1, nums2)   
# print(a) 


def move_one(num,init,des):
    print('move '+str(num)+' from '+init+' to '+des)
    print('---------------------------------')
def hanoi(num,init,temp,des):
    if num==1:
        move_one(num,init,des)
    else:
        hanoi(num-1,init,des,temp)
        move_one(num,init,des)
        hanoi(num-1,temp,init,des)

init, temp, des= 'A','B','C'
hanoi(3, init, temp, des)