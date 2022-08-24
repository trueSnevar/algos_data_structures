# coding: utf-8
# Successful submition: 69752689

from typing import List

def broken_search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] == target:
            return mid
        elif nums[l] <= nums[mid]:
            if nums[l] <= target and nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 
        else:
            if nums[mid] < target and nums[r] >= target:
                l = mid + 1
            else:
                r = mid - 1
    return -1 



def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr2 = [4,5,6,7,0,1,2]
    assert broken_search(arr2, 3) == -1
    arr3 = [1]
    assert broken_search(arr3, 0) == -1

if __name__ == "__main__":
    test()