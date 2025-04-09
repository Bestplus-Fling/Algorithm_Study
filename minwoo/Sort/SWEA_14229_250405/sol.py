import sys
sys.stdin = open('input.txt', 'r')

def quick(nums):
    N = len(nums)
    if N <= 1:
        return nums
    pivot = nums[0]
    left, right = [], []
    for i in range(1, N):
        if pivot > nums[i]:
            left.append(nums[i])
        else:
            right.append(nums[i])
    temp = []
    temp.extend(quick(left))
    temp.append(pivot)
    temp.extend(quick(right))
    return temp


_list = list(map(int, input().split()))
print(quick(_list)[500000])