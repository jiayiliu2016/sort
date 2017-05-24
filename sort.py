#!/usr/bin/python
# -*- coding: utf-8 -*-


# bubblesort
# 大循环： 从第一个元素开始，到最后一个元素
# 小循环： 对所有该小循环中的元素，两两比较元素大小，如果有根据大小，交换两个元素的位置

def bubblesort(arr):
	for i in range (0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]>arr[j]:
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
	return arr



# selectionsort
# 从arr[0]~arr[len(arr)-1]中找出最小的元素及它的的标志位min，将arr[min]与arr[0]交换
# 从arr[1]~arr[len(arr)-1]中找出最小的元素及它的的标志位min，将arr[min]与arr[1]交换

def selectionsort(arr):
	for i in range (0,len(arr)):
		min = i
		for j in range (i+1,len(arr)):
			if arr[min]>arr[j]:
				min=j
		arr[i]=arr[min]
		arr[j]=arr[i]
	return arr



# insertsort
# 对整个序列，从前往后扫描  取待排序序列。 把最后一个元素作为寻找插入位的元素（待排序元素）；
# 对取出的待排序序列，从后往前扫描  寻找插入位置。 当key更小时往前插一位()

def insertionsort(arr):
	for i in range(1,len(arr)):
		j=i-1
		key=arr[i]
		while j>=0:
			if key<arr[j]:
				a[j+1]=a[j]
				j-=1
			arr[j+1]=key
	return arr



# shellsort
# 判断len(list)/3 > (gap=1),才可以用shellsort。 满足时，gap=3*gap+1
# 取 i range in（gap,len(arr)）, 比较 arr[i] a[i-gap]
# 每次 gap=gap/3， 直到 gap=math.floor(gap/3)=0

import math
def shellsort(arr):
	import math
	gap=1
	while(gap<len(arr)/3):
		gap=gap*3+1              # set gap value
	while(gap>0):
		for i in range(gap,len(arr)):       # range(gap,len(arr)) use insertsort
			temp=arr[i]
			j=i-gap
			while j>=o and arr[j]>temp:
				arr[j+gap]=arr[j]
				j-=gap
			arr[j+gap]=temp                
		gap=math.floor(gap/3)            # reflesh gap value
	return arr



# merge sort
# 将待排序序列拆分成更小的子序列
# 序列拆分直到子序列仅剩两个元素 可进行比较并排序，对已排好的两个序列里的元素比较，将取出的较大（或较小）的元素放入一个新的空序列中

def merge(left,right):
	temp=[]
	i=j=0
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			temp.append(left[i])
			i+=1
		else:
			temp.append(right[j])
			j+=1
		if i=len(left):
			for x in right[j:]:
				temp.append(x)
		else if j=len(right):
			for x in left[i:]:
				temp.append(x)
		return temp

def mergesort(arr):
	if len(arr)<2:
		return arr
	middle=len(arr)/2
	left=mergesort(arr[:middle])
	right=mergesort(arr[middle:])
	return merge(left,right)



# quicksort 
# 取出基准元素，比它小的元素放 low[],大的放high[], 并拿到基准元素的标志位key_index（arr[key_index]=key）
# 分别对low[]， high[] 进行快速排序

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)



# heap sort
# 直接选择排序的改进版。 
# 1、建堆：大根堆；2、调堆：A[0]与A[lenth-1]互换，再调整对为大根堆
# 从最后一个非叶子节点i开始，将以i为根节点的二叉树调整为堆 （目标：所有的子树都为堆的完全二叉树）
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
 
def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)
 
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)

    # array = [1, 2, 5, 3, 6, 8, 4]
	# >>> array[::2]
	# [1, 5, 6, 4]
	# >>> array[2::]
	# [5, 3, 6, 8, 4]
	# >>> array[::3]
	# [1, 3, 4]
	# >>> array[::4]
	# [1, 6] 
	# 如果想让他们颠倒形成reverse函数的效果
	# >>> array[::-1]
	# [4, 8, 6, 3, 5, 2, 1]
	# >>> array[::-2]
	# [4, 6, 5, 1]

if __name__ == '__main__':
    arr = raw_input()
    # sort(arr)
    print merge_sort(arr)



