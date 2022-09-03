# coding: utf-8
# doesn't work with TL

import sys

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = merge(nums1, nums2)
    mid = (len(merged)) // 2
    
    if len(merged) % 2 == 0:
        median = (merged[mid-1] + merged[mid]) / 2.0
    else:
        median = merged[mid]
    return median

def merge(nums1, nums2):
    res_arr = []
    l, r = 0,0
    while l < len(nums1) and r < len(nums2):
        if nums1[l] <= nums2[r]:
            res_arr.append(nums1[l])
            l += 1
        else:
            res_arr.append(nums2[r])
            r += 1
            
    while l < len(nums1):
        res_arr.append(nums1[l])
        l += 1
    while r < len(nums2):
        res_arr.append(nums2[r])
        r += 1
    return res_arr

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    #print(findMedianSortedArrays(arr1, arr2))
    res = (findMedianSortedArrays(arr1, arr2))
    sys.stdout.write(str(res))