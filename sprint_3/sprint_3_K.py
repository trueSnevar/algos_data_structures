# coding: utf-8
# https://stackoverflow.com/questions/66284003/problem-implementing-merge-sort-from-pseudo-code-python
# https://contest.yandex.ru/contest/23638/problems/K/?success=69729386#51450/2020_12_13/PtZf82N8yq

def merge(arr, lf, mid, rg):
	left = arr[lf:mid]
	right = arr[mid:rg]
	idx = lf
	l = 0
	r = 0
	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			arr[idx] = left[l]
			l += 1
		else:
			arr[idx] = right[r]
			r += 1
		idx += 1
	while l < len(left):
		arr[idx] = left[l]
		l += 1
		idx += 1
	
	while r < len(right):
		arr[idx] = right[r]
		r += 1
		idx += 1
	return arr

def merge_sort(arr, lf, rg):
	if rg > lf + 1:
		mid = (lf + rg) // 2
		merge_sort(arr, lf, mid)
		merge_sort(arr, mid, rg)
		merge(arr, lf, mid, rg)
	

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == "__main__":
	test()