# 1.插入排序
# 直接插入
def InsertSort(arr):
    if len(arr)>1:
        for i in range(len(arr)):
            j=k=i
            temp = arr[i]
            while j>0 and temp<arr[j-1]:
                arr[j]=arr[j-1]
                print(arr[j])
                j-=1
            arr[j] = temp
            print('k:',j)
            
    return arr



def BinaryInsertSort(arr):
    if len(arr)>1:
        for i in range(len(arr)):
            k,temp = i,arr[i]
            left,right,middle=0,i-1,(0+i)//2
            while left<right:
                if arr[i]>arr[middle]:
                    left = middle+1
                else:
                    right = middle-1
            while k>left:
                arr[k]=arr[k-1]
                k -= 1
            arr[left] = temp
    return arr

arr = [1,5,2,8,3,0,19]
# QuickSort(arr, 0, 6)
# InsertSort(arr)
BinaryInsertSort(arr)
print(arr)                

            


# 折半插入
# 希尔
# 2.交换排序
# 冒泡
# 快排
#quick sort
# def partition(arr,low,high):
#     povit = arr[low]
#     while low<high:
#         while low<high and arr[high]>povit:
#             high-=1
#         arr[low] = arr[high]
#         while low<high and arr[low]<povit:
#             low+=1
#         arr[high] = arr[low]
#     arr[low] = povit
#     return low

# def QuickSort(arr,low,high):

#     if low < high :
#         povit = partition(arr, low, high)
#         QuickSort(arr, low, povit-1)
#         QuickSort(arr, povit+1, high)




# 3.选择排序



#归并排序uio
