# 1.插入排序
# #在一个有序数组中用left，right寻找插入元素的位置时，left的位置总是插入元素的位置
# 直接插入
from array import array
from Tools.demo.sortvisu import bubblesort
def InsertSort(arr):
    if len(arr)>1:
        for i in range(len(arr)):
            j=k=i
            temp = arr[i]
            while j>0 and temp<arr[j-1]:
                arr[j]=arr[j-1]
                j-=1
            arr[j] = temp
    return arr

# 折半插入
#循环中涉及的条件位置不当
def BinaryInsertSort(arr):
    if len(arr)>1:
        for i in range(len(arr)):
            k,temp,left,right = i,arr[i],0,i-1
            while left<=right:
                middle = (left+right)//2
                if arr[i]>arr[middle]:
                    left = middle+1
                else:
                    right = middle-1
            while k>left:
                arr[k]=arr[k-1]
                k -= 1
            arr[left] = temp
    return arr

# 希尔
# 2.交换排序
# 冒泡
def BubbleSort(arr):   
    flag = False
    for i in range(len(arr)):
        j=len(arr)-1-i
        while j>i:
            if arr[j]<arr[j-1]:
                flag = True
                k = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = k
            j -= 1
        if flag != True:
            return arr
    return arr
 
# 快排
# quick sort
# 数组第一个元素为轴，low指向第二个元素，high指向尾，从尾向左找到比povit小的元素放到low的位置，
# 再从low加1向右找到比povit大的元素放到high的位置，最后low的位置放上povit
def partition(arr,low,high):
    povit = arr[low]
    while low<high:
        while low<high and arr[high]>povit:
            high-=1
        arr[low] = arr[high]
        while low<high and arr[low]<povit:
            low+=1
        arr[high] = arr[low]
    arr[low] = povit
    return low
  
def QuickSort(arr,low,high):
    if low < high :
        povit = partition(arr, low, high)
        QuickSort(arr, low, povit-1)
        QuickSort(arr, povit+1, high)

# 3.选择排序
def SelectSort(arr):
    for i in range(len(arr)):
        j = len(arr)-i-1
        small = arr[i]
        #index置为i，防止i位置上元素最小时，index保持上一轮的值
        index = i
        while j > i:
            if arr[j]<small:
                small = arr[j]
                index = j
            j -= 1
        temp = arr[i]
        arr[i] = small
        arr[index] = temp
    return arr
            
#归并排序
# def Merge(arr,left,right):
#     k1 = left
#     k2=middle = (left+right)//2+1
#     tempList = []
#     while (k1<=middle or k2<right):
        
#         if k1>middle and k2<right:
#             for i in range(k2,right+1):
#                 tempList.append(arr[i])
           
#         elif k2>right and k1<middle:
#             for i in range(k1,middle+1):
#                 tempList.append(arr[i])
        
#         else:        
#             if arr[k1]>arr[k2]:
#                 tempList.append(arr[k2])
#                 k2 += 1
#             else:
#                 tempList.append(arr[k1])
#                 k1 += 1
#     k1=k2=0
#     for i in tempList:
#         if k1<=middle:
#             arr[k1]=i
#             k1 += 1
#         else:
#             arr[k2]=i
#             k2 += 1

# def MergeSort(arr,left,right):
#     middle = (left+right)//2
#     if left<right:
#         MergeSort(arr, left,middle)
#         MergeSort(arr, middle+1, right)
#         Merge(arr,left,right)

def Merge(arr1,arr2):
    arr = []
    i,j = 0,0
    while i<len(arr1) or j<len(arr2):
        if i==len(arr1):
            while j<len(arr2):
                arr.append(arr2[j])
                j += 1
        elif j==len(arr2):
            while i<len(arr1):
                arr.append(arr1[i])
                i += 1
        else:
            if arr1[i]<arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
    return arr

#你真的超级厉害！
def MergeSort(arr):
    if len(arr)>1:
        return Merge(MergeSort(arr[0:len(arr)//2]), MergeSort(arr[len(arr)//2:]))
    else:
        return arr
        
    

arr = [1,5,2,8,3,0,19]     
# InsertSort(arr)
# BinaryInsertSort(arr)
# QuickSort(arr, 0, 6)
# BinaryInsertSort(arr)
# SelectSort(arr)
arr = MergeSort(arr)
print(arr) 
         
        
    
    
